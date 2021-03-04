from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'page_numbers', 'publisher', 'is_available', 'rate','created','updated')

admin.site.register(Book, BookAdmin)