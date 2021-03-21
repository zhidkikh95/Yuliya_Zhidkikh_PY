from django.shortcuts import render
from django.views.generic import UpdateView, ListView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from carts import models as cart_models
from accounts import models as account_models
from django.contrib.auth.models import User


from . import models
# Create your views here.
class OrderConfirm(UpdateView):
    model=models.Order
    fields = ('address', 'telephone_number', 'customer_comments')
    def get_object(self, *args, **kwargs):
        current_cart_pk = self.request.session.get('current_cart_pk')
        if not current_cart_pk:
            pass
        else:
            current_cart = cart_models.Cart.objects.get(pk = current_cart_pk)
            current_order_pk = self.request.session.get('current_order_pk')
            current_customer = self.request.user 
            if current_customer.is_anonymous:
                current_customer_profile = None
            else:
                current_customer_profile = account_models.Profile.objects.filter(user = current_customer).first()
                if not current_customer_profile:
                    current_customer_profile = None
            if current_customer and current_customer_profile:
                user_default_data = {
                    'cart': current_cart,
                    'address': current_customer.profile.address,
                    'telephone_number': current_customer.profile.telephone
                }
            else:
                user_default_data = {
                    'cart': current_cart,
                    'address': "",
                    'telephone_number': ""
                } 
            current_order, order_created = models.Order.objects.get_or_create(
                pk = current_order_pk,
                defaults =  user_default_data   
            )
            if order_created:
                self.request.session['current_order_pk'] = current_order.pk
        return current_order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_cart_pk = self.request.session.get('current_cart_pk')
        cart = cart_models.Cart.objects.get(pk=current_cart_pk)
        context["cart"] = cart
        return context

    def get_success_url(self):
        del self.request.session['current_cart_pk']
        del self.request.session['current_order_pk']
        return reverse_lazy('order:success', kwargs={'pk': self.object.pk})

class UserOrder(ListView):
    model = models.Order
    template_name = 'orders/order_user_history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_customer = self.request.user 
        customer_carts = cart_models.Cart.objects.filter(customer = current_customer)
        print(customer_carts)
        user_orders = models.Order.objects.filter(cart__in = customer_carts)
        print(user_orders)
        context["user_orders"] = user_orders
        return context
    
class OrderList(PermissionRequiredMixin, ListView):
    queryset = models.Order.objects.all().order_by('pk')
    queryset = queryset.reverse()
    permission_required = ("orders.view_order", "orders.add_order", "orders.change_order")
    login_url=reverse_lazy('login')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        field_to_sort_on = self.request.GET.get('field')
        direction_to_sort_on = self.request.GET.get('direction')
        context["field_to_sort_on"] = field_to_sort_on
        context["direction_to_sort_on"] = direction_to_sort_on
        return context
    
    def get_ordering(self):
        ordering_by = 'pk'    
        field_to_sort_on = self.request.GET.get('field')
        direction_to_sort_on = self.request.GET.get('direction')
        direction = {'up': ""}
        if field_to_sort_on and direction_to_sort_on:
            ordering_by = f"{direction.get(direction_to_sort_on, '-')}{field_to_sort_on}"
        return ordering_by

class OrderUpdate(PermissionRequiredMixin, UpdateView):
    model = models.Order
    fields = ('address', 'telephone_number', 'customer_comments', 'order_status')
    permission_required = ("orders.view_order", "orders.add_order", "orders.change_order")
    login_url=reverse_lazy('login')
    success_url=reverse_lazy('order:list')
    template_name = 'orders/order_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_order_pk = self.object.pk  
        current_order = models.Order.objects.get(pk=current_order_pk)
        cart = current_order.cart
        context["cart"] = cart
        return context
    
class OrderDetail(DetailView):
    model = models.Order

class OrderSuccess(DetailView):
    model = models.Order
    template_name='orders/order_success.html'

    # class OrderSuccess(RedirectView):
    #     template_name =
    # def get_redirect_url(self, *args, **kwargs):
        
    #     return return_urls.get(action, reverse('cart:add-to-cart'))