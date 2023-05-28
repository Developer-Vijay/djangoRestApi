from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import Company,Employee
from rest_framework.decorators import action
from api.serializers import CompanySerializer,EmployeeSerializer
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
    # companies/{company_id}/employees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            print("methods get executed of employees"   "pk", "company")
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exist || error'
            })
    
       



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer




