from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'cart', 'address', 'customer_comments')

admin.site.register(Order, OrderAdmin)