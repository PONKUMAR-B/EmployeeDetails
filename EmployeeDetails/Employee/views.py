from ast import Delete
from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmployeeDetails
from .models import Employee
from rest_framework.renderers import JSONRenderer


class EmployeeView(APIView):
    def post(self, request):
        serializer = EmployeeDetails(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self,request):
        details = Employee.objects.all()
        serializers = EmployeeDetails(details,many=True)
        return Response(serializers.data)
    
    def put(self, request):
        data = request.data
        emp = Employee.objects.get(id = data['id'])
        serializer = EmployeeDetails(emp, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request):
        data = request.data
        emp = Employee.objects.get(id = data['id']).delete()
        return Response("successfully deleted",emp.data,content_type='application/json')
      