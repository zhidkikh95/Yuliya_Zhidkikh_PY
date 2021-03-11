from django.urls import path

from . import views

urlpatterns = [
    path('authors/', views.AuthorList.as_view(), name='author-list'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author-details'),
    path('author/delete/<int:pk>/', views.AuthorDelete.as_view(), name='author-delete'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/update/<int:pk>/', views.AuthorUpdate.as_view(), name='author-update'),
    path('publishers/', views.PublisherList.as_view(), name='publisher-list'),
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisher-details'),
    path('publisher/delete/<int:pk>/', views.PublisherDelete.as_view(), name='publisher-delete'),
    path('publisher/create/', views.PublisherCreate.as_view(), name='publisher-create'),
    path('publisher/update/<int:pk>/', views.PublisherUpdate.as_view(), name='publisher-update'),
    path('genres/', views.GenreList.as_view(), name='genre-list'),
    path('genre/delete/<int:pk>/', views.GenreDelete.as_view(), name='genre-delete'),
    path('genre/create/', views.GenreCreate.as_view(), name='genre-create'),
    path('genre/update/<int:pk>/', views.GenreUpdate.as_view(), name='genre-update'),
    path('book-series/', views.BookSeriesList.as_view(), name='book-series-list'),
    path('book-series/delete/<int:pk>/', views.BookSeriesDelete.as_view(), name='book-series-delete'),
    path('book-series/create/', views.BookSeriesCreate.as_view(), name='book-series-create'),
    path('book-series/update/<int:pk>', views.BookSeriesUpdate.as_view(), name='book-series-update')  
]
  
