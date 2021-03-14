from . models import Cart

def harvest_data(cbv_obj):
    """Harvest all the data from the request

    Args:
        cbv_obj ([cbv object]):
    Returns:
        [tuple]: (current_cart_pk, cart_items}   
    """

    current_cart_pk = cbv_obj.request.session.get('current_cart_pk')
    cart_items = cbv_obj.request.GET
    return current_cart_pk, cart_items


def update_items_in_cart(cart_items_from_form, current_cart_pk):
    # action = None
    cart = Cart.objects.filter(pk=current_cart_pk).first()
    if not cart:
        return
    items = cart.books.all()
    for book_pk, quantity  in cart_items_from_form.items():
        if book_pk == 'btn':
            continue
            # action = quantity 
        item = items.filter(pk=book_pk).first()
        if item and int(quantity) > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()
    # return action