from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

from medpack.bagpack.utils import get_active_cart
from medpack.orders.api.serializers import OrderSerializer,Order
from medpack.orders.utils import cart_order


class OrderListApiView(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderCreateApiView(APIView):
    def post(self,request):
        cart=get_active_cart(request.user)
        if cart.items.all().exists():
            order=cart_order(cart)
            serializer=OrderSerializer(instance=order)
            return Response(serializer.data)
        raise NotFound()
