from .models import Company,Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields =['eFname', 'eLname', 'eCompany', 'eEmail', 'ePhone']
        # fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields =['cName', 'cLogo', 'cUrl', 'cEmail']
        # fields = '__all__'