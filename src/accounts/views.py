from django.shortcuts import render
from django.contrib.auth import authenticate, login, views, logout
# Create your views here.

class MyLoginView(views.LoginView):
    template_name="accounts/login.html"