from django.db import models
import json

# Create your models here.

class Employee(models.Model):
	name = models.CharField(max_length=200)
	hiring_date = models.DateTimeField('hiring date')
	email = models.EmailField() 
	salary = models.IntegerField()
	cell_phone = models.IntegerField()
	manager = models.ForeignKey("self", on_delete=models.SET_NULL, related_name='self', null=True)

	def __str__(self):
		return self.name

	def total_managed_salary(self):
		return self.salary + 1
	
	def toJSON(self):
	        return json.dumps(self, default=lambda o: o.__dict__, 
	            sort_keys=True, indent=4)

	class Meta:
		db_table = 'employees'
		verbose_name = 'Employee'
		verbose_name_plural = 'Employees'