from django.db import models
 
# Create your models here.

class Order(models.Model):
    cart = models.OneToOneField(
        "carts.Cart",
        verbose_name = "Корзина пользователя",
        on_delete=models.PROTECT)

    address = models.TextField(
        verbose_name = "Адрес доставки")

    telephone_number = models.CharField(
        verbose_name="Контактный номер",
        max_length=15)
    
    customer_comments = models.TextField(
        verbose_name = "Комментарии к заказу",
        blank = True,
        null = True)

    def __str__(self):
        return self.cart
    
