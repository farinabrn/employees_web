FROM python:3.7-alpine
MAINTAINER Bruno Farina

ENV PYTHONUNBUFFERED 1

COPY . .

RUN apk add --no-cache --virtual build-dependencies \
	python3-dev \
	mysql-dev \
	py-mysqldb \
	libxslt-dev \
	mariadb-dev \
	build-base \
	libc-dev \
	libffi-dev \
	bash \
	gcc \
	g++ \
	musl-dev \
    && pip3 install --no-cache-dir -r requirements.txt \
    && apk del build-dependencies

RUN apk -q --no-cache add musl zlib mariadb-common mariadb-client mariadb-connector-c-dev

EXPOSE 8000

COPY entrypoint.sh .
ENTRYPOINT ["sh", "entrypoint.sh"]
