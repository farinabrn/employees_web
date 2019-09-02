from django.urls import path

from . import views_api
from . import views

app_name = 'employees'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:employee_id>/', views.detail, name='detail'),
	path('api/employees/', views_api.employee_list),
	path('api/employees/<int:pk>', views_api.employee_detail),
]
