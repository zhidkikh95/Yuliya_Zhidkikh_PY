from django.db import models
import datetime

# Create your models here.

class Order(models.Model):
    cart = models.OneToOneField(
        "carts.Cart",
        verbose_name = "Корзина пользователя",
        on_delete=models.PROTECT,
        related_name = 'orders'
    )

    address = models.TextField(
        verbose_name = "Адрес доставки")

    telephone_number = models.CharField(
        verbose_name="Контактный номер",
        max_length=15)
    
    customer_comments = models.TextField(
        verbose_name = "Комментарии к заказу",
        blank = True,
        null = True)
    
    created = models.DateTimeField(
        verbose_name="Дата заказа",
        auto_now_add=True,
        blank = True,
        null = True)
   
    open_order = 'Новый'
    processed_order = 'В обработке'
    closed_order = 'Закрыт'
    cancelled_order = 'Отменен'
    order_status_choices = [(open_order, "Новый"), (processed_order, "В обработке"), (closed_order, "Закрыт"), (cancelled_order, 'Отменен')]

    order_status = models.CharField(
        verbose_name="Статус заказа",
        choices = order_status_choices,
        default = open_order,
        max_length = 20) 

    # def __str__(self):
    #     return self.cart.customer
    
