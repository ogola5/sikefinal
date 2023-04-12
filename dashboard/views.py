from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

# Create your views here.
def dashboard(request):
    context = {}
    return render(request, 'posApp/dashboard.html',context)