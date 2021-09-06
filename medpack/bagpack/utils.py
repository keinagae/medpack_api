from medpack.bagpack.models import BagPackStatus, BagPack


def get_active_cart(user):
    cart, _ = BagPack.objects.get_or_create(user=user, status=BagPackStatus.ACTIVE)
    return cart
