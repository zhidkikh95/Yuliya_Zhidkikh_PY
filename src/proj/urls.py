"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dictionaries import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home-page'),
    path('authors', views.AuthorList.as_view(), name='author-list'),
    path('author/<int:pk>', views.AuthorDetail.as_view(), name='author-details'),
    path('author-delete/<int:pk>', views.AuthorDelete.as_view(), name='author-delete'),
    path('author-create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author-update/<int:pk>', views.AuthorUpdate.as_view(), name='author-update'),
    path('publishers', views.PublisherList.as_view(), name='publisher-list'),
    path('publisher/<int:pk>', views.PublisherDetail.as_view(), name='publisher-details'),
    path('publisher-delete/<int:pk>', views.PublisherDelete.as_view(), name='publisher-delete'),
    path('publisher-create/', views.PublisherCreate.as_view(), name='publisher-create'),
    path('publisher-update/<int:pk>', views.PublisherUpdate.as_view(), name='publisher-update'),
    path('genres', views.GenreList.as_view(), name='genre-list'),
    path('genre-delete/<int:pk>', views.GenreDelete.as_view(), name='genre-delete'),
    path('genre-create/', views.GenreCreate.as_view(), name='genre-create'),
    path('genre-update/<int:pk>', views.GenreUpdate.as_view(), name='genre-update'),
    path('book-series', views.BookSeriesList.as_view(), name='book-series-list'),
    path('book-series-delete/<int:pk>', views.BookSeriesDelete.as_view(), name='book-series-delete'),
    path('book-series-create/', views.BookSeriesCreate.as_view(), name='book-series-create'),
    path('book-series-update/<int:pk>', views.BookSeriesUpdate.as_view(), name='book-series-update')
]
