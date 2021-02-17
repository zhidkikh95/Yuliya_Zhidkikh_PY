from django.shortcuts import render
from dictionaries.models import Author, Publisher, Genre, BookSeries
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.urls import  reverse_lazy

class AuthorDetail(DetailView):
    model=Author

class AuthorList(ListView):
    model=Author

class AuthorDelete(DeleteView):
    model=Author
    success_url=reverse_lazy('author-list')

class AuthorCreate(CreateView):
    model=Author
    fields=("surname","name","patronymic", "country", "birthdate", "biography") 
    success_url=reverse_lazy('author-list')

class AuthorUpdate(UpdateView):
    model=Author
    fields=("surname","name","patronymic", "country", "birthdate", "biography") 
    success_url=reverse_lazy('author-list')

class PublisherList(ListView):
    model=Publisher

class PublisherDetail(DetailView):
    model=Publisher

class PublisherDelete(DeleteView):
    model=Publisher
    success_url=reverse_lazy('publisher-list')

class PublisherCreate(CreateView):
    model=Publisher    
    fields=("publisher_name", "publisher_description")
    success_url=reverse_lazy('publisher-list')

class PublisherUpdate(UpdateView):
    model=Publisher    
    fields=("publisher_name", "publisher_description")
    success_url=reverse_lazy('publisher-list')

class GenreList(ListView):
    model=Genre

class GenreDelete(DeleteView):
    model=Genre
    success_url=reverse_lazy('genre-list')

class GenreCreate(CreateView):
    model=Genre
    fields=('genre_name',)
    success_url=reverse_lazy('genre-list')

class GenreUpdate(UpdateView):
    model=Genre
    fields=('genre_name',)
    success_url=reverse_lazy('genre-list')

class BookSeriesList(ListView):
    model=BookSeries

class BookSeriesDelete(DeleteView):
    model=BookSeries
    success_url=reverse_lazy('book-series-list')

class BookSeriesCreate(CreateView):
    model=BookSeries
    fields=('series_name',)
    success_url=reverse_lazy('book-series-list')

class BookSeriesUpdate(UpdateView):
    model=BookSeries
    fields=('series_name',)
    success_url=reverse_lazy('book-series-list')


