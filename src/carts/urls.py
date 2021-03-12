from django.urls import path

from . import views
app_name='cart'

urlpatterns = [
    path('user-cart/', views.UserCart.as_view(), name='user-cart'),
    path('add-to-cart/', views.UpdateCart.as_view(), name='add-to-cart')
]
