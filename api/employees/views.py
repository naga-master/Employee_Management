from rest_framework import generics
from .models import Employees
from .serializers import EmployeeDetailSerializer, EmployeeNameSerializer, \
   EmployeeUpdateSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly



# Create your views here.
class ListEmployeesView(generics.ListAPIView):
   '''
   Description: list all employees details in detail
   '''
   queryset = Employees.objects.all() # get all fields
   serializer_class = EmployeeDetailSerializer # serialize all fields , except owner
   throttle_scope = 'employee_app'
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
class ListEmployeesName(generics.ListAPIView):
   '''
   Description: list all employees names 
   '''
   queryset = Employees.objects.all() # get all fields
   serializer_class = EmployeeNameSerializer # serialize name field only 
   throttle_scope = 'employee_app'
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CreateEmployee(generics.CreateAPIView):
   '''
   Description: create a new employee
   '''
   queryset = Employees.objects.all() # get all fields
   serializer_class = EmployeeDetailSerializer # serialize all fields , except owner
   throttle_scope = 'employee_app'
   # can post only if user logged in
   permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 

   def perform_create(self, serializer):
      '''
      Description: set owner field as a user logged in
      '''
      serializer.save(owner=self.request.user)

class UpdateEmployee(generics.UpdateAPIView):
   queryset = Employees.objects.all() # get all fields
   serializer_class = EmployeeUpdateSerializer # serialize only designation field
   throttle_scope = 'employee_app'
   #  can put only if user logged in
   permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 

   def perform_create(self, serializer):
      '''
      Description: set owner field as a user logged in
      '''
      serializer.save(owner=self.request.user)

class DeleteEmployee(generics.DestroyAPIView):
   queryset = Employees.objects.all() # get all fields
   serializer_class = EmployeeDetailSerializer # serialize all fields , except owner
   throttle_scope = 'employee_app'
   #  can delete only if user logged in
   permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 


   def perform_create(self, serializer):
      '''
      Description: set owner field as a user logged in
      '''
      serializer.save(owner=self.request.user)
