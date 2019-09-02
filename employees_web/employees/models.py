from django.db import models
import json

# Create your models here.

class Employee(models.Model):
	name = models.CharField(max_length=200)
	hiring_date = models.DateTimeField('hiring date')
	email = models.EmailField() 
	salary = models.IntegerField()
	cell_phone = models.IntegerField()
	manager = models.ForeignKey('self', null=True, on_delete=models.SET_NULL, related_name='subordinate')

	def __str__(self):
		return self.name

	def get_managed_count(self, id=None):
		if id is None:
			id = self.id

		managed_list = Employee.objects.filter(manager=self)
		managed_count=0
		for employee in managed_list:
			managed_count+=employee.get_managed_count(id)

		if self.id != id:
			managed_count+=1

		return managed_count

	def get_managed_salary(self, id=None):
		if id is None:
			id = self.id

		managed_list = Employee.objects.filter(manager=self)
		managed_salary=0
		for employee in managed_list:
			managed_salary+=employee.get_managed_salary(id)

		if self.id != id:
			managed_salary+=self.salary

		return managed_salary
	
	def toJSON(self):
	        return json.dumps(self, default=lambda o: o.__dict__, 
	            sort_keys=True, indent=4)

	class Meta:
		db_table = 'employees'
		verbose_name = 'Employee'
		verbose_name_plural = 'Employees'