from django.shortcuts import render
from dictionaries.models import Author, Publisher, Genre, BookSeries
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from django.db.models import Q
from books import models
from . import forms

def home_page(request):
    return render(request, template_name="base.html")

class AuthorDetail(DetailView):
    model=Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_author = self.object
        current_author_books = models.Book.objects.filter(author = current_author)
        context["current_author_books"] = current_author_books
        return context
    

class AuthorList( ListView):
    model=Author
    # login_url=reverse_lazy('login')
    # permission_required = ("dictionaries.view_author", "dictionaries.delete_author", "dictionaries.add_author", "dictionaries.change_author")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        field_to_sort_on = self.request.GET.get('field')
        direction_to_sort_on = self.request.GET.get('direction')
        print(field_to_sort_on, direction_to_sort_on)
        context["field_to_sort_on"] = field_to_sort_on
        context["direction_to_sort_on"] = direction_to_sort_on
        query = self.request.GET.get('query')
        context['search_form'] = forms.SearchForm(
            initial={
                'query': query,
                'field': field_to_sort_on,      
                'direction': direction_to_sort_on
            })
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
           query_set = query_set.filter(Q(surname__icontains=query)|Q(name__icontains=query)) 
        return query_set

class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model=Author
    success_url=reverse_lazy('author-list')
    login_url=reverse_lazy('login')
    permission_required = "dictionaries.delete_author"

class AuthorCreate(PermissionRequiredMixin, CreateView):
    model=Author
    fields=("surname","name","patronymic", "country", "birthdate", "biography") 
    success_url=reverse_lazy('author-list')
    login_url=reverse_lazy('login')
    permission_required = "dictionaries.add_author"

class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model=Author
    fields=("surname","name","patronymic", "country", "birthdate", "biography") 
    success_url=reverse_lazy('author-list')
    login_url=reverse_lazy('login')
    permission_required =  "dictionaries.change_author"

class PublisherList(PermissionRequiredMixin, ListView):
    model=Publisher
    login_url=reverse_lazy('login')
    permission_required = ("dictionaries.view_publisher", "dictionaries.delete_publisher", "dictionaries.add_publisher", "dictionaries.change_publisher")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        field_to_sort_on = self.request.GET.get('field')
        direction_to_sort_on = self.request.GET.get('direction')
        print(field_to_sort_on, direction_to_sort_on)
        context["field_to_sort_on"] = field_to_sort_on
        context["direction_to_sort_on"] = direction_to_sort_on
        query = self.request.GET.get('query')
        context['search_form'] = forms.SearchForm(
            initial={
                'query': query,
                'field': field_to_sort_on,      
                'direction': direction_to_sort_on
            })
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
           query_set = query_set.filter(publisher_name__icontains=query) 
        return query_set

class PublisherDetail(PermissionRequiredMixin, DetailView):
    model=Publisher
    login_url=reverse_lazy('login')
    permission_required = "dictionaries.view_publisher"

class PublisherDelete(PermissionRequiredMixin, DeleteView):
    model=Publisher
    success_url=reverse_lazy('publisher-list')
    login_url=reverse_lazy('login')
    permission_required = "dictionaries.delete_publisher"

class PublisherCreate(PermissionRequiredMixin, CreateView):
    model=Publisher    
    fields=("publisher_name", "publisher_description")
    success_url=reverse_lazy('publisher-list')
    login_url=reverse_lazy('login')
    permission_required = "dictionaries.add_publisher"

class PublisherUpdate(PermissionRequiredMixin,UpdateView):
    model=Publisher    
    fields=("publisher_name", "publisher_description")
    success_url=reverse_lazy('publisher-list')
    login_url=reverse_lazy('login')
    permission_required = "dictionaries.change_publisher"

class GenreList(PermissionRequiredMixin, ListView):
    model=Genre
    login_url=reverse_lazy('login')
    permission_required = ("dictionaries.view_genre", "dictionaries.delete_genre", "dictionaries.add_genre", "dictionaries.change_genre")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        field_to_sort_on = self.request.GET.get('field')
        direction_to_sort_on = self.request.GET.get('direction')
        print(field_to_sort_on, direction_to_sort_on)
        context["field_to_sort_on"] = field_to_sort_on
        context["direction_to_sort_on"] = direction_to_sort_on
        query = self.request.GET.get('query')
        context['search_form'] = forms.SearchForm(
            initial={
                'query': query,
                'field': field_to_sort_on,      
                'direction': direction_to_sort_on
            })
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
           query_set = query_set.filter(genre_name__icontains=query) 
        return query_set

class GenreDelete(PermissionRequiredMixin, DeleteView):
    model=Genre
    success_url=reverse_lazy('genre-list')
    login_url=reverse_lazy('login')
    permission_required = "dictionaries.delete_genre"

class GenreCreate(PermissionRequiredMixin, CreateView):
    model=Genre
    fields=('genre_name',)
    success_url=reverse_lazy('genre-list')
    login_url=reverse_lazy('login')
    permission_required = "dictionaries.add_genre"

class GenreUpdate(PermissionRequiredMixin, UpdateView):
    model=Genre
    fields=('genre_name',)
    success_url=reverse_lazy('genre-list')
    login_url=reverse_lazy('login')
    permission_required = "dictionaries.change_genre"

class BookSeriesList(PermissionRequiredMixin, ListView):
    model=BookSeries
    login_url=reverse_lazy('login')
    permission_required = ("dictionaries.view_bookseries", "dictionaries.delete_bookseries", "dictionaries.add_bookseries", "dictionaries.change_bookseries")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        field_to_sort_on = self.request.GET.get('field')
        direction_to_sort_on = self.request.GET.get('direction')
        print(field_to_sort_on, direction_to_sort_on)
        context["field_to_sort_on"] = field_to_sort_on
        context["direction_to_sort_on"] = direction_to_sort_on
        query = self.request.GET.get('query')
        context['search_form'] = forms.SearchForm(
            initial={
                'query': query,
                'field': field_to_sort_on,      
                'direction': direction_to_sort_on
            })
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
           query_set = query_set.filter(series_name__icontains=query) 
        return query_set

class BookSeriesDelete(PermissionRequiredMixin, DeleteView):
    model=BookSeries
    success_url=reverse_lazy('book-series-list')
    login_url=reverse_lazy('login')
    permission_required = "dictionaries.delete_bookseries"

class BookSeriesCreate(PermissionRequiredMixin, CreateView):
    model=BookSeries
    fields=('series_name',)
    success_url=reverse_lazy('book-series-list')
    login_url=reverse_lazy('login')
    permission_required = "dictionaries.add_bookseries"

class BookSeriesUpdate(PermissionRequiredMixin, UpdateView):
    model=BookSeries
    fields=('series_name',)
    success_url=reverse_lazy('book-series-list')
    login_url=reverse_lazy('login')
    permission_required = "dictionaries.change_bookseries"


