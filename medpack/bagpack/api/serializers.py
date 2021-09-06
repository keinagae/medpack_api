from rest_framework import serializers
from medpack.bagpack.models import BagPack,BagPackItem
from medpack.products.api.serializers import ProductSerializer,Product


class BagPacItemSerializer(serializers.ModelSerializer):
    product=ProductSerializer(read_only=True)
    product_id=serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),source="product",write_only=True)

    class Meta:
        model=BagPackItem
        fields=[
            "id",
            "product",
            "quantity",
            'product_id'
        ]

class BagPackSerializer(serializers.ModelSerializer):
    items=BagPacItemSerializer(many=True)
    class Meta:
        model=BagPack
        fields=[
            "user",
            "status",
            'items'
        ]
