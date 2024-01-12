from django.shortcuts import render
from django.http import HttpResponse
# from datetime import datetime
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class HomeView(TemplateView):
    template_name = 'homeapp/welcome.html'

# def home(request):
#     return render(request, 'homeapp/welcome.html', {'today': datetime.today})

class AuthorizedViews(LoginRequiredMixin, TemplateView):
    template_name = 'homeapp/authorized.html'
    login_url = '/admin'

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'homeapp/authorized.html', {'today': datetime.today})