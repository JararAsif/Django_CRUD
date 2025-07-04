from django.db import models

# Create your models here.
class Employee(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name= models.CharField(max_length=30)
    Emp_id=models.IntegerField(max_length=20,unique=True)

def __str__(self):
    return self.First_Name+" "+self.Last_Name

