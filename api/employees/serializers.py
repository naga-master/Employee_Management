from django.db.models import fields
from rest_framework import serializers
from .models import Employees


class EmployeeDetailSerializer(serializers.ModelSerializer):
   class Meta:
      model = Employees
      fields = ["id", "name", "age", "email_id", "designation"]


class EmployeeNameSerializer(serializers.ModelSerializer):
   class Meta:
      model = Employees
      fields = ["name", ]


class EmployeeUpdateSerializer(serializers.ModelSerializer):
   class Meta:
      model = Employees
      fields = ["designation",]
      
