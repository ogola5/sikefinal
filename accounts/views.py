from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .forms import UserRegistrationForm, UserAddressForm


User = get_user_model()


class UserRegistrationView(TemplateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'accounts/user_registration.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(
                reverse_lazy('transactions:transaction_report')
            )
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        registration_form = UserRegistrationForm(self.request.POST)
        address_form = UserAddressForm(self.request.POST)

        if registration_form.is_valid() and address_form.is_valid():
            user = registration_form.save()
            address = address_form.save(commit=False)
            address.user = user
            address.save()

            login(self.request, user)
            messages.success(
                self.request,
                (
                    f'Thank You For Creating A Bank Account. '
                    f'Your Account Number is {user.account.account_no}. '
                )
            )
            return HttpResponseRedirect(
                reverse_lazy('transactions:deposit_money')
            )

        return self.render_to_response(
            self.get_context_data(
                registration_form=registration_form,
                address_form=address_form
            )
        )

    def get_context_data(self, **kwargs):
        if 'registration_form' not in kwargs:
            kwargs['registration_form'] = UserRegistrationForm()
        if 'address_form' not in kwargs:
            kwargs['address_form'] = UserAddressForm()

        return super().get_context_data(**kwargs)


class UserLoginView(LoginView):
    template_name='accounts/user_login.html'
    redirect_authenticated_user = False


class LogoutView(RedirectView):
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super().get_redirect_url(*args, **kwargs)
    
@api_view(['GET', 'POST'])
def User_list(request, format=None):

    if request.method =='GET':
     user = User.objects.all()
     serializer = UserSerializer(user, many=True)
     return Response(serializer.data)
    
    if request.method =='POST':
      serializer = UserSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

@api_view(['GET', 'PUT', 'DELETE'])
def User_detail(request, id, format=None):
        try:
           
           user = User.objects.get(pk=id)
        except User.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        if request.method == 'GET':
          serializer = UserSerializer(user)
          return Response(serializer.data)
        elif request.method == 'PUT':
          serializer = UserSerializer(user, data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

        elif request.method == 'DELETE':
           user.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)   
        

@api_view(['GET', 'POST'])
def BankAccountType_list(request, format=None):

    if request.method =='GET':
     bankAccountType = BankAccountType.objects.all()
     serializer = BankAccountTypeSerializer(bankAccountType, many=True)
     return Response(serializer.data)
    
    if request.method =='POST':
      serializer = BankAccountTypeSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

@api_view(['GET', 'PUT', 'DELETE'])
def BankAccountType_detail(request, id, format=None):
        try:
           
           bankAccountType = BankAccountType.objects.get(pk=id)
        except BankAccountType.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        if request.method == 'GET':
          serializer = UserSerializer(bankAccountType)
          return Response(serializer.data)
        elif request.method == 'PUT':
          serializer = BankAccountTypeSerializer(bankAccountType, data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

        elif request.method == 'DELETE':
           bankAccountType.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)   

@api_view(['GET', 'POST'])
def UserBankAccount_list(request, format=None):

    if request.method =='GET':
     userbankAccount = UserBankAccount.objects.all()
     serializer = UserBankAccountSerializer(userbankAccount, many=True)
     return Response(serializer.data)
    
    if request.method =='POST':
      serializer = UserBankAccountSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

@api_view(['GET', 'PUT', 'DELETE'])
def UserBankAccount_detail(request, id, format=None):
        try:
           
           userbankAccount = UserBankAccount.objects.get(pk=id)
        except UserBankAccount.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        if request.method == 'GET':
          serializer = UserSerializer(userbankAccount)
          return Response(serializer.data)
        elif request.method == 'PUT':
          serializer = UserBankAccountSerializer(userbankAccount, data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

        elif request.method == 'DELETE':
           userbankAccount.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)   
        
        
@api_view(['GET', 'POST'])
def UserAddress_list(request, format=None):

    if request.method =='GET':
     userAddress = UserAddress.objects.all()
     serializer = UserAddressSerializer(userAddress, many=True)
     return Response(serializer.data)
    
    if request.method =='POST':
      serializer = UserAddressSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

@api_view(['GET', 'PUT', 'DELETE'])
def UserAddress_detail(request, id, format=None):
        try:
           
           userAddress = UserAddress.objects.get(pk=id)
        except UserAddress.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        if request.method == 'GET':
          serializer = UserSerializer(userAddress)
          return Response(serializer.data)
        elif request.method == 'PUT':
          serializer = UserAddressSerializer(userAddress, data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

        elif request.method == 'DELETE':
           userAddress.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)   
        
        


