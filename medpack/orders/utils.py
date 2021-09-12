from medpack.bagpack.models import BagPack, BagPackStatus
from .models import Order,OrderItem

def cart_order(cart:BagPack):
    order=Order.objects.create(user=cart.user)
    for cart_item in cart.items.all():
        order.items.create(product=cart_item.product,quantity=cart_item.quantity)
        cart_item.product.quantity-=cart_item.quantity
        cart_item.product.save()
    cart.status=BagPackStatus.ORDERED
    cart.save()
    return order
