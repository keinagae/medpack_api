from rest_framework.generics import RetrieveAPIView,CreateAPIView
from .serializers import BagPackSerializer,BagPack,BagPacItemSerializer
from medpack.bagpack.models import BagPackStatus
from ..utils import get_active_cart


class ItemToCartApiView(CreateAPIView):
    serializer_class = BagPacItemSerializer

    def perform_create(self, serializer):
        cart=get_active_cart(self.request.user)
        instance=cart.items.create(**serializer.validated_data)
        return instance



class CartApiView(RetrieveAPIView):
    serializer_class = BagPackSerializer
    def get_object(self):
        return get_active_cart(self.request.user)

