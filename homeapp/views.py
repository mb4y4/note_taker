from django.shortcuts import render
from django.http import HttpResponse
# from datetime import datetime
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

class LoginInterfaceView(LoginView):
    template_name = 'homeapp/login.html'
    
class LogoutInterfaceView(LogoutView):
    template_name = 'homeapp/logout.html'
    
class HomeView(TemplateView):
    template_name = 'homeapp/welcome.html'



