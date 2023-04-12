from django.urls import path,include
from . import views
from .views import *
from django.views.generic.base import TemplateView
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'mirai'

urlpatterns=[
    path('', views.dashboard, name="dashboard"),
    path('admin/', admin.site.urls),
    path('comp', views.comp),
    path('show', views.show),
    path('edit/<str:cName>', views.edit),
    path('update/<str:cName>', views.update),
    path('delete/<str:cName>', views.delete), 
    path('emp', views.emp),
    path('showemp', views.showemp),
    path('deleteEmp/<str:eFname>', views.deleteEmp),
    path('editemp/<str:eFname>', views.editemp), 
    path('updateEmp/<str:eFname>', views.updateEmp),
    path('company/', views.Company_list),
    path('company/<int:id>',views.Company_detail),
    path('employee/', views.Employee_list),
    path('employee/<int:id>',views.Employee_detail),
    path('accounts/', include('django.contrib.auth.urls')),
]