from django.urls import path

from . import views

urlpatterns = [
    path('login', views.MyLoginView.as_view(), name='login'),
    path('logout', views.MyLogoutView.as_view(), name='logout'),
    path('register', views.register, name = 'register'),
    path('profile/<int:pk>', views.UserUpdate.as_view(), name="user-update"),
    path('profile/update/', views.UserProfileUpdate.as_view(), name="user-profile-update"),
]
