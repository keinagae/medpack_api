from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .serializers import ProductSerializer,Product


class ProductListApiView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

class MyProductViewSet(ModelViewSet):
    serializer_class=ProductSerializer
    parser_classes = (MultiPartParser,)
    def get_queryset(self):
        return Product.objects.filter(provider=self.request.user)

    def perform_create(self,serializer):
        serializer.validated_data['provider']=self.request.user
        return serializer.save()
