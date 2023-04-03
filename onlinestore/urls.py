from django.urls import path
from django.contrib import admin
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout1/', views.checkout1, name="checkout1"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('Customers/', views.Customer_list),
    path('Customers/', views.Customer_detail),
    path('Products/', views.Product_list),
    path('Products/<int:id>', views.Product_detail),
    path('Orders/', views.Order_list),
    path('Orders/<int:id>', views.Order_detail),
    path('Order-items/', views.OrderItem_list),
    path('Order-items/<int:id>', views.OrderItem_detail),
    path('Shipping-addresss/', views.ShippingAddress_list),
    path('Shipping-addresss/<int:id>', views.ShippingAddress_detail),

]
urlpatterns = format_suffix_patterns(urlpatterns)