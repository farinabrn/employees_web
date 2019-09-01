sudo apt-get update
sudo apt-get -y install mysql-server
mysql_secure_installation
mysql -u root -e "employees_web" -p;
mysql -u root -p employees_web < db.sql
sudo apt-get install libmysqlclient-dev