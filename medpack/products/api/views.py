from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .serializers import ProductSerializer,Product
from medpack.products.models import ProductStatusEnum


class ProductListApiView(ListAPIView):
    serializer_class = ProductSerializer

    permission_classes = []

    search_fields = ['name', 'description']

    def get_queryset(self):
        return Product.objects.filter(quantity__gt=0,status__in=[ProductStatusEnum.PENDING,ProductStatusEnum.APPROVED]).order_by("-id")

class MyProductViewSet(ModelViewSet):
    serializer_class=ProductSerializer
    parser_classes = (MultiPartParser,)
    def get_queryset(self):
        return Product.objects.filter(provider=self.request.user).order_by("-id")

    def perform_create(self,serializer):
        serializer.validated_data['provider']=self.request.user
        return serializer.save()
