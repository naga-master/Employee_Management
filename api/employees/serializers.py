from django.db.models import fields
from rest_framework import serializers
from .models import Employees

class EmployeeDetailSerializer(serializers.ModelSerializer):
   class Meta:
      model = Employees
      fields = "__all__"


class EmployeeNameSerializer(serializers.ModelSerializer):
   class Meta:
      model = Employees
      fields = ("id", "name")


      
