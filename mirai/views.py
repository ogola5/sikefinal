from django.shortcuts import render,redirect
from mirai.models import Company,Employee
from mirai.forms import CompanyForm,EmployeeForm
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeeSerializer,CompanySerializer
from django.http import JsonResponse



# Create your views here.

class TableViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class=EmployeeSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class=CompanySerializer

#def loginCheck(request):
    #if request.method == 'POST':
        #username = request.POST['username']
        #password = request.POST['password']

        #user = auth.authenticate(username = username, password = password)
        #if user is not None:
            #auth.login(request, user)
            #return redirect("/emp")
        #else:
            #messages.info(request, 'invalid credentials')
            #return redirect



    #else:
        #form = loginForm()
        #return render(request, "regsitration/login.html")


@api_view(['GET', 'POST'])
def Company_list(request):
    if request.method =='GET':
        employee = Company.objects.all()
        serializer = CompanySerializer(employee, many=True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     
      
@api_view(['GET', 'PUT', 'DELETE'])
def Company_detail(request, id, format=None):
        try:
           
           company = Company.objects.get(pk=id)
        except Company.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        if request.method == 'GET':
          serializer = CompanySerializer(company)
          return Response(serializer.data)
        elif request.method == 'PUT':
          serializer = CompanySerializer(company, data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

        elif request.method == 'DELETE':
           company.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Employee_list(request):
    if request.method =='GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
@api_view(['GET', 'PUT', 'DELETE'])
def Employee_detail(request, id, format=None):
        try:
           
           employee = Employee.objects.get(pk=id)
        except Employee.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        if request.method == 'GET':
          serializer = EmployeeSerializer(employee)
          return Response(serializer.data)
        elif request.method == 'PUT':
          serializer = EmployeeSerializer(employee, data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

        elif request.method == 'DELETE':
           employee.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)


#Home page
def home(request):
    return redirect(request,"")


# To create Company
def comp(request):
    if request.method == "POST":

        form = CompanyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = CompanyForm()
    return render(request, "index.html", {'form':form})

# To retrieve Company details
def show(request):
    companies = Company.objects.all()
    return render(request, "show.html", {'companies':companies})

# To Edit Company details
def edit(request, cName):
    company = Company.objects.get(cName=cName)
    return render(request, "edit.html", {'company':company})

# To Update Company
def update(request, cName):
    company = Company.objects.get(cName=cName)
    form = CompanyForm(request.POST, instance= company)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, "edit.html", {'company': company})

# To Delete Company details
def delete(request, cName):
    company = Company.objects.get(cName=cName)
    company.delete()
    return redirect("/show")

def dashboard(request):
    return render(request, 'dashboard.html')

# def dashboard(request):
#     # context = {}
   
#     return render(request "dashboard.html")


# To create employee
def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/showemp")
            # try:
            #     form.save()
            #     return redirect("/showemp")
            # except:
            #     print(f"Error saving form data")
            #     return HttpResponse("Error saving form data. Please try again later.")
    else:
        form = EmployeeForm()
    return render(request, "addemp.html", {'form':form})

# To show employee details
def showemp(request):
    employees = Employee.objects.all()
    return render(request, "showemp.html", {'employees':employees})

# To delete employee details
def deleteEmp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    employee.delete()
    return redirect("/showemp")

# To edit employee details
def editemp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    return render(request, "editemployee.html", {'employee':employee})

# To update employee details
def updateEmp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    form = EmployeeForm(request.POST, instance= employee)
    print('Hello1')
    if form.is_valid():
        
        form.save()
        return redirect("/showemp")
    return render(request, "editemployee.html", {'employee': employee})

