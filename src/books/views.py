import random

from django.shortcuts import render
from books.models import Book
from dictionaries.models import Author
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.urls import  reverse_lazy

class BookList(ListView):
    model=Book

class HomePage(ListView):
    queryset = Book.objects.all().order_by('pk')
    queryset = queryset.reverse()[:5]
    template_name='books/home_page.html'  
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['number'] = random.randint(1, 100)
    #     return context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors=Author.objects.all().order_by('pk')
        authors=authors.reverse()[:5]
        context['authors'] = authors
        return context

class BookDetail(DetailView):
    model=Book

class BookCreate(CreateView):
    model=Book
    fields=("name", "book_picture", "price", "author", "genre", "series", "publisher", "published_year", "page_numbers", "binding", "book_format", "isbn_num", "weight", "age_restriction", "available_number", "is_available", "rate") 
    success_url=reverse_lazy('book-list')

class BookUpdate(UpdateView):
    model=Book
    fields=("name", "book_picture", "price", "author", "genre", "series", "publisher", "published_year", "page_numbers", "binding", "book_format", "isbn_num", "weight", "age_restriction", "available_number", "is_available", "rate") 
    success_url=reverse_lazy('book-list')
    # login_url='admin/'
    # permission_required =  "dictionaries.change_author"
