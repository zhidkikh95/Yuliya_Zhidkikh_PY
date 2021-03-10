from django.contrib import admin
from .models import Cart, BookInCart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer')

admin.site.register(Cart, CartAdmin)

class BookInCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'book', 'quantity')

admin.site.register(BookInCart, BookInCartAdmin)