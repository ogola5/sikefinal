from store.models import Product
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
import json
import datetime
from django.contrib import messages
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# def signup(request):
#     if request.method=='POST':
#          form = signupform(request.POST)
#          if form.is_valid():
#               form.save
#               return redirect('login')
#     else:
#          form = signupform()

#     return render(request, 'store/signup.html',{'form':form})

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('login')
#     else:
#         form = UserCreationForm()

#     return render(request, 'store/signup.html', {'form': form})



# def Login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('store')
#         else:
#             messages.error(request, 'Invalid username or password')
    
#     return render(request, 'store/login.html')


# def Login(request):
#     if request.method=="POST":
#          username = request.POST['username']
#          password = request.POST['password']

#          user = authenticate(username=username,password=password)
#          if user is not None:
#               login(request,user)
#               return redirect('next/')
#     else:
#       return render(request, 'store/login.html')



def next(request):
    context = {}
    return render(request, 'store/next.html', context)


def store(request):
    data = cartData(request)

    cartItems = data['cartItems']   
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
    data = cartData(request)
	
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)

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