from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .serializers import ProductSerializer,Product


class ProductListApiView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

class MyProductViewSet(ModelViewSet):
    serializer_class=ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(provider=self.request.user)
