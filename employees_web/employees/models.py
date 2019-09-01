from django.db import models

# Create your models here.

class Employee(models.Model):
	name = models.CharField(max_length=200)
	hiring_date = models.DateTimeField('hiring date')
	email = models.EmailField() 
	salary = models.IntegerField()
	cell_phone = models.IntegerField()
	deleted = models.BooleanField(default=False)
	manager = models.ForeignKey("self", on_delete=models.SET_NULL, related_name='self', null=True)

	def __str__(self):
		return self.name

	def total_managed_salary(self):
		return self.salary + 1

	class Meta:
		index_together = ["name", "deleted"]
		db_table = 'employees'
		verbose_name = 'Employee'
		verbose_name_plural = 'Employees'