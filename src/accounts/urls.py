from django.urls import path

from . import views

urlpatterns = [
    path('login', views.MyLoginView.as_view(), name='login'),
    path('logout', views.MyLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', views.UserProfile.as_view(), name="user-profile"),
    path('profile/update/<int:pk>', views.UserProfileUpdate.as_view(), name="user-profile-update"),
]
