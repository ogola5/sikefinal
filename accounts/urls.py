from django.urls import path

from .views import UserRegistrationView, LogoutView, UserLoginView
from . import views




app_name = 'accounts'

urlpatterns = [
    path(
        "", UserLoginView.as_view(),
        name="user_login"
    ),
    path(
        "logout/", LogoutView.as_view(),
        name="user_logout"
    ),
    path(
        "register/", UserRegistrationView.as_view(),
        name="user_registration"
    ),
    path('user', views.User_list),
    path('user/<int:id>', views.User_detail),
    path('mm/', views.BankAccountType_list),
    path('bankAccountType/<int:id>', views.BankAccountType_detail),
    path('userBankAccout/', views.UserBankAccount_list),
    path('userBankAccount/<int:id>', views.UserBankAccount_detail),
    path('userAddress/', views.UserAddress_list),
    path('userAddress/<int:id>', views.UserAddress_detail)
  

]
