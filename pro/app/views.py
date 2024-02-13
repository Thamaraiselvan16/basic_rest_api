from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from .forms import EmployeeForm


@api_view(["GET","POST"])

def emp_list(request, format=None):
    if request.method=="GET":
        emp=Employee.objects.all()
        serializer=EmployeeSerializer(emp, many=True)
        return Response(serializer.data)
        # return render(request, 'emp_list.html',{'employee_data': serializer.data})  #🔴🔴 template
    
    elif request.method=="POST":
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return render(request, 'emp_add.html',{'employee_data': serializer.data})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
@api_view(["GET","PUT","DELETE"])
def emp_detail(request, id, format=None):
    try:
        emp=Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serializer=EmployeeSerializer(emp)
        return Response(serializer.data)
        # return render(request, 'emp_detail.html',{'employee_details': serializer.data})
    
    elif request.method=="PUT":
        serializer=EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=="DELETE":
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        