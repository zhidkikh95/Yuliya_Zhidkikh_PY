from django.shortcuts import render
from django.views.generic import DetailView, RedirectView, UpdateView
from . import models, utils 
from books import models as book_models
from django.contrib.auth import get_user_model
from django.urls import reverse
 
User = get_user_model()

class UpdateCart(DetailView):
    model = models.Cart
    template_name = "carts/add-to-cart.html"

    def get_object(self, *args, **kwargs):
        book_id = self.request.GET.get('book')
        if not book_id:
            current_cart_pk = self.request.session.get('current_cart_pk')
            if current_cart_pk:
                current_cart = models.Cart.objects.filter(pk=current_cart_pk).first()
                return current_cart or []
            return []
        else:
            current_cart_pk = self.request.session.get('current_cart_pk')
            current_customer=self.request.user
            if current_customer.is_anonymous:
                current_customer = None
            current_cart, cart_created = models.Cart.objects.get_or_create(
                pk = current_cart_pk,
                defaults = {'customer': current_customer}    
            )
            if cart_created:
                self.request.session['current_cart_pk'] = current_cart.pk
            book = book_models.Book.objects.get(pk=book_id)
            price = book.price
            book_in_cart, book_created = models.BookInCart.objects.get_or_create(
                cart = current_cart,
                book = book,
                price = price,
                defaults = {'quantity': 1}
            )
            book_in_cart.save()
            if not book_created:
                book_in_cart.quantity += 1
                book_in_cart.save()
        print(current_cart)
        return current_cart

class ReсalculateCart(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        current_cart_pk, cart_items = utils.harvest_data(self)
        current_cart_pk_for_url = self.request.session.get('current_cart_pk')
        return_urls = {
            'checkout': reverse('order:checkout', kwargs={'cart_pk': current_cart_pk_for_url})
        }
        if not current_cart_pk: 
            return reverse('cart:add-to-cart')
        action = utils.update_items_in_cart(cart_items, current_cart_pk)
        
        return return_urls.get(action, reverse('cart:add-to-cart'))
