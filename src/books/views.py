import random

from django.shortcuts import render
from books.models import Book
from dictionaries.models import Author
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import  reverse_lazy

class BookList(ListView):
    model=Book
    paginate_by=10

class HomePage(ListView):
    queryset = Book.objects.all().order_by('pk')
    queryset = queryset.reverse()[:5]
    template_name='books/home_page.html'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors=Author.objects.all().order_by('pk')
        authors=authors.reverse()[:5]
        context['authors'] = authors
        return context

class BookDetail(DetailView):
    model=Book

class BookCreate(PermissionRequiredMixin, CreateView):
    model=Book
    fields=("name", "book_picture", "price", "author", "genre", "series", "publisher", "published_year", "page_numbers", "binding", "book_format", "isbn_num", "weight", "age_restriction", "available_number", "is_available", "rate") 
    success_url=reverse_lazy('book-list')
    login_url=reverse_lazy('login')
    permission_required = "books.add_book"

class BookUpdate(PermissionRequiredMixin, UpdateView):
    model=Book
    fields=("name", "book_picture", "price", "author", "genre", "series", "publisher", "published_year", "page_numbers", "binding", "book_format", "isbn_num", "weight", "age_restriction", "available_number", "is_available", "rate") 
    success_url=reverse_lazy('book-list')
    login_url=reverse_lazy('login')
    permission_required = "books.change_book"
