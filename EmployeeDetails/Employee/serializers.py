from dataclasses import field
from .models import Employee
from rest_framework import serializers

class EmployeeDetails(serializers.ModelSerializer):
    # eno=serializers.IntegerField()
    # ename=serializers.CharField(max_length=100)
    # esalary=serializers.IntegerField()
    # eaddress=serializers.CharField(max_length=100)

    class Meta:
        model=Employee
        fields="__all__"