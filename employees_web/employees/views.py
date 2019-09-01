from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def index(request):
	employee_list = Employee.objects.order_by('name')
	data = {'employee_list': employee_list}
	return render(request, 'employees/index.html', data)

	# if request.method == "POST":
	# 	form = EmployeeForm(request.POST)
	# 	if form.is_valid():
	# 		try:
	# 			form.save()
	# 			return redirect('/show')
	# 		except:
	# 			pass

	# else:
	# 	form = EmployeeForm()

	# return render(request,'employees/index.html', {'form': form})



def detail(request, employee_id):
	employee = get_object_or_404(Employee, pk=employee_id)
	return render(request, 'employees/detail.html', {'employee': employee})
