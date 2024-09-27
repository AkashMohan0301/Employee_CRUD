from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Fuction Based Model -----------------------------------------------------------------------
@api_view(['GET', 'POST', 'PUT','DELETE', 'PATCH'])

def EmployeeView(request):
    if request.method == 'GET':
        employeeData = Employee.objects.all()
        try :
            if employeeData.exists():
                serializer = EmployeeSerializer(employeeData, many=True)
                return Response({"Status": "OK",'data': serializer.data})
        except :
            return Response({"Status": "Empty",'data': 'No data found'})

    if request.method =='POST':
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status": "Created",'data': serializer.data})
        else :
            return Response({"Status": "Validation Error",'data': serializer.errors})

    if request.method == 'PUT':
        employee = Employee.objects.get(pk=request.data['id'])
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status": "Updated",'data': serializer.data})
        else :
            return Response({"Status": "Validation Error",'data': serializer.errors})

    if request.method == 'PATCH':
        employee = Employee.objects.get(pk=request.data['id'])
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status": "Updated",'data': serializer.data})
        else :
            return Response({"Status": "Validation Error",'data': serializer.errors})


    if request.method == 'DELETE':
        employee_id = request.data['id']
        if Employee.objects.filter(pk=employee_id).exists():
            employee = Employee.objects.get(pk=employee_id)
            employee.delete()
            return Response({"Status": "Deleted"})
        else:
            return Response({"Status": "Employee does not exist"})




# clall Based View
from rest_framework.views import APIView

class EmployeeViewClass(APIView):
    def get(self,request):
        employeeData = Employee.objects.all()
        try :
            if employeeData.exists():
                serializer = EmployeeSerializer(employeeData,many=True)
                return Response(serializer.data)
        except:
            return Response({"Status": "No data"})
    
    def post(self,request):
        serializer = EmployeeSerializer(data = request.data)
        try:
            # Create a new Person object
            serializer = EmployeeSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response({"error": "An unexpected error occurred"})


    def patch(self,request):
        employee = Employee.objects.get(pk = request.data.get('id'))
        serializer = EmployeeSerializer(employee, data = request.data, partial = True)

    def patch(self, request):
        try:
            employee = Employee.objects.get(pk=request.data.get('id'))

        except Employee.DoesNotExist:
            return Response({"error": "Employee does not exist"})
        
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,request):
        employee_id = request.data['id']
        if Employee.objects.filter(pk = employee_id).exists():
            employee = Employee.objects.get(pk = employee_id)
            employee.delete()
            return Response({"Status": "Deleted"})
        else:
            return Response({"Status": "Employee does not exist"})





class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()  # Define the queryset for the viewset
    serializer_class = EmployeeSerializer  # Specify the serializer to be used
