from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import json

# Create your models here.

class Employee(MPTTModel):
	STANDARD = 'STD'
	MANAGER = 'MGR'
	SR_MANAGER = 'SRMGR'
	PRESIDENT = 'PRES'

	EMPLOYEE_TYPES = (
		(STANDARD, 'base employee'),
		(MANAGER, 'manager'),
		(SR_MANAGER, 'senior manager'),
		(PRESIDENT, 'president')
	)

	name = models.CharField(max_length=200)
	hiring_date = models.DateTimeField('hiring date')
	email = models.EmailField() 
	salary = models.IntegerField()
	cell_phone = models.IntegerField()
	role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES, default=STANDARD)
	parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subordinate')

	def __str__(self):
		return self.name

	def get_managed_count(self):
		return self.get_descendants().count()

	def get_managed_salary(self, id=None):
		if id is None:
			id = self.id

		managed_salary=0
		for employee in self.subordinate.all():
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