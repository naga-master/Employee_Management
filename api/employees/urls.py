from django.urls import path
from .views import ListEmployeesView, ListEmployeesName, CreateEmployee, \
UpdateEmployee, DeleteEmployee

urlpatterns = [	
	path('Employees/', ListEmployeesName.as_view(), name="all-employees"),
	path('EmployeeDetails/', ListEmployeesView.as_view(), name="employees-all"),
	path('CreateEmployee/', CreateEmployee.as_view(), name="create-employee"),
	path('UpdateEmployee/<int:pk>', UpdateEmployee.as_view(), name="update-employee"),
	path('DeleteEmployee/<int:pk>', DeleteEmployee.as_view(), name="delete-employee"),
]
