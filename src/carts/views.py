from django.shortcuts import render
from django.views.generic import DetailView
from . import models 
from books import models as book_models
from django.contrib.auth import get_user_model
User = get_user_model()

class UpdateCart(DetailView):
    model = models.Cart
    template_name = "carts/add-to-cart.html"

    def get_object(self, *args, **kwargs):
        book_id = self.request.GET.get('book')
        print(book_id)
        if not book_id:
            # throw an error
            pass
        else:
            current_cart_pk = self.request.session.get('current_cart_pk')
            print(current_cart_pk)
            current_customer=self.request.user
            if current_customer.is_anonymous:
                current_customer = None
            current_cart, cart_created = models.Cart.objects.get_or_create(
                pk = current_cart_pk,
                defaults = {'customer': current_customer}    
            )
            print(cart_created, current_cart_pk)
            if cart_created:
                self.request.session['current_cart_pk'] = current_cart.pk
            book = book_models.Book.objects.get(pk=book_id)
            book_in_cart, book_created = models.BookInCart.objects.get_or_create(
                cart = current_cart,
                book = book,
                defaults = {'quantity': 1}
            )
            if not book_created:
                book_in_cart.quantity += 1
                book_in_cart.save()
        return current_cart

class UserCart(DetailView):
    model = models.Cart
    template_name = "carts/user-cart.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     current_customer=self.request.user
    #     current_cart_pk = self.request.session.get('current_cart_pk')
    #     if current_customer.is_anonymous:
    #         current_customer = None
    #     current_cart_pk = models.Cart.objects.get(
    #         customer = current_customer)
    #     books_in_cart = models.BookInCart.objects.filter(cart = current_cart_pk)
    #     context["books_in_cart"] = books_in_cart
    #     # total_amount = books_in_cart.book.price*books_in_cart.quantity
    #     # context['total_amount'] = total_amount
    #     return context

    def get_object(self, *args, **kwargs):
        current_cart_pk = self.request.session.get('current_cart_pk')
        current_customer=self.request.user
        if current_customer.is_anonymous:
            current_customer = None
        if not current_cart_pk:
            current_cart, cart_created = models.Cart.objects.get_or_create(
                pk = current_cart_pk,
                defaults = {'customer': current_customer}    
            )
            if cart_created:
                self.request.session['current_cart_pk'] = current_cart.pk
        else:
            current_cart = models.Cart.objects.get(pk = current_cart_pk)

        return current_cart

