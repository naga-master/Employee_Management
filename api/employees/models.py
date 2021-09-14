from django.db import models

# Create your models here.

class Employees(models.Model):
   id = models.IntegerField(primary_key=True, null=False)
   name = models.CharField(max_length=255, null=False)
   age = models.IntegerField(null=False)
   email_id = models.EmailField(max_length=255)
   designation = models.CharField(max_length=255, null=False)
   

   def __str__(self):
      return "{} - {} - {} - {} - {}".format(self.id, self.name, 
         self.age, self.email_id, self.designation)
