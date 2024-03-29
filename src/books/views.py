import random

from django.shortcuts import render
from books.models import Book
from dictionaries.models import Author
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.urls import  reverse_lazy
from . import forms

class BookList(ListView):
    model=Book
    paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # authors=Author.objects.all().order_by('pk')
        # authors=authors.reverse()[:5]
        field_to_sort_on=self.request.GET.get('field')
        direction_to_sort_on=self.request.GET.get('direction')
        query = self.request.GET.get('query')
        context['search_form'] = forms.SearchForm(
            initial={
                'query': query,
                'field': field_to_sort_on,      
                'direction': direction_to_sort_on
            })

        context['field_to_sort_on'] = field_to_sort_on
        context['direction_to_sort_on'] = direction_to_sort_on
        return context

    def get_ordering(self):
        ordering_by = 'pk'    
        field_to_sort_on = self.request.GET.get('field')
        direction_to_sort_on = self.request.GET.get('direction')
        direction = {'up': ""}
        if field_to_sort_on and direction_to_sort_on:
            ordering_by = f"{direction.get(direction_to_sort_on, '-')}{field_to_sort_on}"
        return ordering_by
    
    def get_queryset(self):
        query = self.request.GET.get('query')
        query_set = super().get_queryset()
        if query:
            author = Author.objects.all()
            # authorname= author.filter
            query_set = query_set.filter(name__icontains=query) 
            # query_set = query_set.filter(Q(name__icontains=query)| Q(author__icontains=query)) 
        return query_set
    

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
