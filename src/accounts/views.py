from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth import authenticate, login, views, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import  reverse_lazy, reverse
from django.contrib.auth import get_user_model
from accounts.models import Profile
from accounts.forms import UserCreationForm

User = get_user_model()
# Create your views here.

class MyLoginView(views.LoginView):
    template_name="accounts/login.html"

class MyLogoutView(views.LogoutView):
    next_page=reverse_lazy('home-page')

class UserProfile(DetailView):
    model = User
    template_name="accounts/user_detail.html"

def register(request):
    if request.method == "GET":
        return render(
            request, 'accounts/register.html',
            {"form": UserCreationForm}
        )
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('user-profile-update'))
        return render(request, 'accounts/register.html', {'form': form})

   

class UserUpdate(UpdateView):
    model = User
    template_name="accounts/user_form.html"
    fields=('username', 'email', 'first_name', 'last_name')

    def get_object(self, *args, **kwargs):
        user = self.request.user
        return user

    def get_success_url(self):
        current_user=self.request.user
        return reverse_lazy('home-page')



class UserProfileUpdate( UpdateView):
    model = Profile
    template_name="accounts/user_profile_form.html"
    fields = ('telephone', 'address')
    success_url = reverse_lazy('home-page')

    def get_object(self, *args, **kwargs):
        user = self.request.user
        profile, profile_created= Profile.objects.get_or_create(
            user = user
        ) 
        return profile
