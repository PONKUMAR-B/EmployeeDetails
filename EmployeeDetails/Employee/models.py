from django.db import models

# Create your models here.

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esalary=models.IntegerField()
    eaddress=models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)
