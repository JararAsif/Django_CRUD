from django.db import models


# Create your models here.
class Department(models.Model):
    name= models.CharField(max_length=30)
    description = models.TextField(blank=True)
    code=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name
    


class Employee(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name= models.CharField(max_length=30)
    department_name=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.First_Name+" "+self.Last_Name
    






