from rest_framework import serializers

from medpack.products.models import Product,Variant,VariantAttribute,VariantAttributeValues

class VariantAttributeValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantAttributeValues
        fields=[
            "id",
            "value"
        ]

class VariantAttributeSerializer(serializers.ModelSerializer):

    values=VariantAttributeValuesSerializer(many=True)

    class Meta:
        model = VariantAttribute
        fields=[
            "id",
            "name",
            "values"
        ]

class VariantsSerializer(serializers.ModelSerializer):
    attributes=VariantAttributeSerializer(many=True)
    class Meta:
        model=Variant
        fields=[
            "id",
            'name',
            'quantity',
            "attributes"
        ]


class ProductSerializer(serializers.ModelSerializer):
    variants=VariantsSerializer(many=True,allow_null=True)
    class Meta:
        model=Product
        fields=[
            "id",
            "name",
            "expiry_date",
            "status",
            "provider",
            "image",
            "description",
            "variants"
        ]
