from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'homeapp/signup.html'
    success_url = '/smart/notes/'
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

class LoginInterfaceView(LoginView):
    template_name = 'homeapp/login.html'
    
class LogoutInterfaceView(LogoutView):
    template_name = 'homeapp/logout.html'
    
class HomeView(TemplateView):
    template_name = 'homeapp/welcome.html'



