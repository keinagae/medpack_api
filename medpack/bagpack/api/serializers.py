from django.db.models import F
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


    def create(self, validated_data):
        bagpack=validated_data['bagpack']
        instance, _ = bagpack.items.get_or_create(product=validated_data['product'])
        instance.quantity += validated_data['quantity']
        instance.save()
        if instance.quantity<=0:
            instance.delete()
        return instance

class BagPackSerializer(serializers.ModelSerializer):
    items=BagPacItemSerializer(many=True)
    class Meta:
        model=BagPack
        fields=[
            "user",
            "status",
            'items'
        ]
