from rest_framework import serializers

from medpack.products.api.serializers import ProductSerializer
from medpack.orders.models import Order,OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product=ProductSerializer(read_only=True)

    class Meta:
        model=OrderItem
        fields=[
            "id",
            "product",
            "quantity",
        ]

class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True)
    class Meta:
        model=Order
        fields=[
            "id",
            "user",
            'status',
            'items',
            "created_at"
        ]
