from django.shortcuts import render
from books.models import Book
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
# Create your views here.

class BookList(ListView):
    model=Book