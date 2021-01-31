from django.contrib import admin
from .models import Author, Genre, Publisher, BookSeries

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'country','birthdate', 'biography')

admin.site.register(Author, AuthorAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre_name',)

admin.site.register(Genre, GenreAdmin)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('publisher_name', 'publisher_description')

admin.site.register(Publisher, PublisherAdmin)

class BookSeriesAdmin(admin.ModelAdmin):
    list_display = ('series_name',)

admin.site.register(BookSeries, BookSeriesAdmin)