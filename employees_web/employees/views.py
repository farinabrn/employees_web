from django.shortcuts import render, get_object_or_404
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.

def index(request):
	employee_list = Employee.objects.order_by('name')
	data = {'employee_list': employee_list}
	return render(request, 'employees/index.html', data)

def detail(request, employee_id):
	employee = get_object_or_404(Employee, pk=employee_id)
	return render(request, 'employees/detail.html', {'employee': employee})