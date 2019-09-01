from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employee

# Create your views here.

def index(request):
	employee_list = Employee.objects.order_by('-hiring_date')
	context = {'employee_list': employee_list}
	return render(request, 'employees/index.html', context)


def detail(request, employee_id):
	employee = get_object_or_404(Employee, pk=employee_id)
	return render(request, 'employees/detail.html', {'employee': employee})
