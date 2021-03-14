from django.urls import path

from . import views
app_name='cart'

urlpatterns = [
    path('add-to-cart/', views.UpdateCart.as_view(), name='add-to-cart'),
    path('recalculate-cart/', views.ReсalculateCart.as_view(), name='recalculate-cart'),
    path('checkout/<int:pk>/', views.Checkout.as_view(), name='checkout'),
]
