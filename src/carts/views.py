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
        print(book_id)
        if not book_id:
            current_cart_pk = self.request.session.get('current_cart_pk')
            if current_cart_pk:
                current_cart = models.Cart.objects.filter(pk=current_cart_pk).first()
                return current_cart or []
            return []
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

class ReсalculateCart(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # return_urls={
        #     'checkout': reverse('cart:add-to-cart')
        # }
        current_cart_pk, cart_items = utils.harvest_data(self)
        if not current_cart_pk: 
            return reverse('cart:add-to-cart')
        utils.update_items_in_cart(cart_items, current_cart_pk)
        # action = utils.update_items_in_cart(cart_items, current_cart_pk)
        return reverse('cart:add-to-cart')
        # return_urls.get(action )
# reverse('cart:checkout', kwargs={'pk': current_cart_pk})
class Checkout(UpdateView): 
    models = models.BookInCart
    fields = ('book', 'price', 'quantity')