from django.shortcuts import render

from rest_framework import generics
from .models import Employees
from .serializers import EmployeeDetailSerializer, EmployeeNameSerializer

# Create your views here.
class ListEmployeesView(generics.ListAPIView):
   queryset = Employees.objects.all()
   serializer_class = EmployeeDetailSerializer
   
   

class ListEmployeesName(generics.ListAPIView):
   queryset = Employees.objects.all()
   serializer_class = EmployeeNameSerializer

class CreateEmployee(generics.CreateAPIView):
   queryset = Employees.objects.all()
   serializer_class = EmployeeDetailSerializer

class UpdateEmployee(generics.UpdateAPIView):
   queryset = Employees.objects.all()
   serializer_class = EmployeeDetailSerializer

class DeleteEmployee(generics.DestroyAPIView):
   queryset = Employees.objects.all()
   serializer_class = EmployeeDetailSerializer

