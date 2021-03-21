from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('history/', views.UserOrder.as_view(), name = 'history'),
    path('checkout/<int:cart_pk>/', views.OrderConfirm.as_view(), name='checkout'),
    path('list/', views.OrderList.as_view(), name = 'list'),
    path('update/<int:pk>/', views.OrderUpdate.as_view(), name = 'update'),
    path('detail/<int:pk>/', views.OrderDetail.as_view(), name = 'detail'),
    path('success/<int:pk>/', views.OrderSuccess.as_view(), name = 'success'),

    
]