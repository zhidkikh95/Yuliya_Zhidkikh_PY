from django.urls import path

from . import views

urlpatterns = [
    path('detail/<int:pk>', views.BookDetail.as_view(), name="book-details"),
    path('create/', views.BookCreate.as_view(), name="book-create"),
    path('list/', views.BookList.as_view(), name="book-list"),   
    path('update/<int:pk>', views.BookUpdate.as_view(), name="book-update"),
]
