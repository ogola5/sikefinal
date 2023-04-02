
#from onlinestore.models import Product
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import requests
import datetime
from rest_framework import status

from rest_framework import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import cookieCart, cartData, guestOrder

def store(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'posApp/store.html', context)

def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'items':items, 'order':order, 'cartItems':cartItems }
	return render(request, 'posApp/cart.html', context)

def checkout1(request):
 data = cartData(request)
	
 cartItems = data['cartItems']
 order = data['order']
 items = data['items']
 context = {'items':items, 'order':order, 'cartItems':cartItems}
 return render(request, 'posApp/checkout1.html', context)


def updateItem(request):
  data = json.loads(request.body)
  productId = data['productId']
  action = data['action']
  print('Action:', action)
  print('Product:', productId)

  customer = request.user.customer
  product = Product.objects.get(id=productId)
  order, created = Order.objects.get_or_create(customer=customer, complete=False)

  orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	
  if action == 'add':
    orderItem.quantity = (orderItem.quantity + 1)
	
  elif action == 'remove':
    orderItem.quantity = (orderItem.quantity - 1)

  orderItem.save()

  if orderItem.quantity <= 0:
    orderItem.delete()

  return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

@api_view(['GET', 'POST'])
def Customer_list(request, format=None):

    if request.method =='GET':
     Customers = Customer.objects.all()
     serializer = CustomerSerializer(Customers, many=True)
     return Response(serializer.data)
    
    if request.method =='POST':
      serializer = CustomerSerializer(data=request.data)
      if serializer.is_valid():
       serializer.save()
       
       return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def Customer_detail(request, id, format=None):
        try:
           
           customer = Customer.objects.get(pk=id)
        except Customer.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        if request.method == 'GET':
          serializer = CustomerSerializer(customer)
          return Response(serializer.data)
        elif request.method == 'PUT':
          serializer = CustomerSerializer(customer, data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
           customer.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def Product_list(request, format=None):

    if request.method =='GET':
     Products = Product.objects.all()
     serializer = ProductSerializer(Products, many=True)
     return Response(serializer.data)
    
    if request.method =='POST':
      serializer = ProductSerializer(data=request.data)
      if serializer.is_valid():
       serializer.save()
       
       return Response(serializer.data, status = status.HTTP_201_CREATED)

    
    # if request.method == 'POST':
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     # If the serializer is not valid, return a response with the errors
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Product_detail(request, id, format=None):
        try:
           
           product = Product.objects.get(pk=id)
        except Product.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        if request.method == 'GET':
          serializer = ProductSerializer(product)
          return Response(serializer.data)
        elif request.method == 'PUT':
          serializer = ProductSerializer(product, data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
           product.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET', 'POST'])
def Order_list(request, format=None):

    if request.method =='GET':
     Orders = Order.objects.all()
     serializer = OrderSerializer(Orders, many=True)
     return Response(serializer.data)
    
    if request.method =='POST':
      serializer = OrderSerializer(data=request.data)
      if serializer.is_valid():
       serializer.save()
       
       return Response(serializer.data, status = status.HTTP_201_CREATED) 


@api_view(['GET', 'PUT', 'DELETE'])
def Order_detail(request, id, format=None):
        try:
           
           order = Order.objects.get(pk=id)
        except Order.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        if request.method == 'GET':
          serializer = OrderSerializer(order)
          return Response(serializer.data)
        elif request.method == 'PUT':
          serializer = OrderSerializer(order, data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
           order.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def OrderItem_list(request, format=None):

    if request.method =='GET':
     orderitems = OrderItem.objects.all()
     serializer = OrderItemSerializer(orderitems, many=True)
     return Response(serializer.data)
    
    if request.method =='POST':
      serializer = OrderItemSerializer(data=request.data)
      if serializer.is_valid():
       serializer.save()
       
       return Response(serializer.data, status = status.HTTP_201_CREATED) 


@api_view(['GET', 'PUT', 'DELETE'])
def OrderItem_detail(request, id, format=None):
        try:
           
           orderitems = OrderItem.objects.get(pk=id)
        except Order.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        if request.method == 'GET':
          serializer = OrderItemSerializer(orderitems)
          return Response(serializer.data)
        elif request.method == 'PUT':
          serializer = OrderItemSerializer(orderitems, data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
           orderitems.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)  

@api_view(['GET', 'POST'])
def ShippingAddress_list(request, format=None):

    if request.method =='GET':
     Shippingaddress = ShippingAddress.objects.all()
     serializer = ShippingAddressSerializer(Shippingaddress, many=True)
     return Response(serializer.data)
    
    if request.method =='POST':
      serializer = ShippingAddressSerializer(data=request.data)
      if serializer.is_valid():
       serializer.save()
       
       return Response(serializer.data, status = status.HTTP_201_CREATED) 


@api_view(['GET', 'PUT', 'DELETE'])
def ShippingAddress_detail(request, id, format=None):
        try:
           
           shippingaddress = ShippingAddress.objects.get(pk=id)
        except ShippingAddress.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        if request.method == 'GET':
          serializer = ShippingAddressSerializer(shippingaddress)
          return Response(serializer.data)
        elif request.method == 'PUT':
          serializer = ShippingAddressSerializer(shippingaddress, data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
           shippingaddress.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)                    



