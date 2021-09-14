from django.core import validators
from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.exceptions import ValidationError

def validateAge(value:str):
   if '-' in value:
      raise ValidationError('Enter Valid Age non negative')
   elif len(value) > 3:
      raise ValidationError('Enter Valid Age 0-100')
   else:
      return value

class Employees(models.Model):
   '''
   Description: create database fields
   '''
   id = models.IntegerField(unique=True, primary_key=True, null=False)
   name = models.CharField(max_length=255, null=False)
   age = models.CharField(max_length=3, null=False, validators=[validateAge])
   email_id = models.EmailField(max_length=255)
   designation = models.CharField(max_length=255, null=False)
   owner = models.ForeignKey('auth.user', related_name='Employees', 
         on_delete= models.CASCADE)
   

   def __str__(self):
      return "{} - {} - {} - {} - {}".format(self.id, self.name, 
         self.age, self.email_id, self.designation)



