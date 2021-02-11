from django.shortcuts import render
from dictionaries.models import Author
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