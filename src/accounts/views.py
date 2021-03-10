from django.shortcuts import render
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth import authenticate, login, views, logout
from django.urls import  reverse_lazy
from django.contrib.auth import get_user_model
from accounts.models import Profile
User = get_user_model()
# Create your views here.

class MyLoginView(views.LoginView):
    template_name="accounts/login.html"

class MyLogoutView(views.LogoutView):
    next_page=reverse_lazy('home-page')

class UserProfile(DetailView):
    model = User
    template_name="accounts/user_detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     current_user = self.request.user
    #     print(current_user)
    #     telephone = current_user.profile.telephone
    #     address = current_user.profile.address
    #     print(telephone, address)
    #     context["telephone"] = telephone
    #     context["address"] = address
    #     return context

   

class UserProfileUpdate(UpdateView):
    model = User
    template_name="accounts/user_form.html"
    fields=('username', 'email', 'first_name', 'last_name')
    def get_success_url(self):
        current_user=self.request.user
        return reverse_lazy('user-profile', kwargs={'pk': current_user.pk})