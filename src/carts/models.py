from django.db import models
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.PROTECT, 
        verbose_name="Корзина пользователя",
        related_name="cart",
        blank=False,
        null=True
    )
    def __str__(self):
        return f"Корзина {self.customer}"

class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart, 
        verbose_name="Корзина пользователя",
        related_name="books", 
        on_delete=models.CASCADE)
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.PROTECT,
        verbose_name="Товары в корзине" 
    )
    quantity = models.IntegerField(
        verbose_name = "Колечество товара",
        default = 1)
    def __str__(self):
        return f"{self.book} в корзине {self.cart}"