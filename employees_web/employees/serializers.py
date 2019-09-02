from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = ('name', 'hiring_date', 'email', 'salary', 'cell_phone', 'manager')

		def create(self, validated_data):
			return Employee.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.name = validated_data.get('name', instance.name)
			instance.hiring_date = validated_data.get('hiring_date', instance.hiring_date)
			instance.email = validated_data.get('email', instance.email)
			instance.salary = validated_data.get('salary', instance.salary)
			instance.cell_phone = validated_data.get('cell_phone', instance.cell_phone)
			instance.manager = validated_data.get('manager', instance.manager)

			instance.save()
			return instance
