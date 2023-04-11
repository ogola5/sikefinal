from django.urls import path
from . import views


urlpatterns = [
    # path('', views.signup, name="signup"),
    # path('next/', views.next, name="next"),
    # path('login/', views.Login, name="login"),
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    #  path('signup/', views.signup, name="signup"),
    # path('next/', views.next, name="next"),
    # path('login/', views.Login, name="login"),
]