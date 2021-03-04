from django.shortcuts import render
from django.contrib.auth import authenticate, login, views, logout
from django.urls import  reverse_lazy
# Create your views here.

class MyLoginView(views.LoginView):
    template_name="accounts/login.html"

class MyLogoutView(views.LogoutView):
    next_page=reverse_lazy('home-page')