from django.urls import path

from . import views

app_name = 'employees'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:employee_id>/', views.detail, name='detail'),
]
