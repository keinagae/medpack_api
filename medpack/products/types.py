import graphene
from graphene_django import DjangoObjectType
from medpack.products.models import Product

class ProductType(DjangoObjectType):
    class Meta:
        model=Product
        fields=[
            "name","description","image","expiry_date"
        ]
        filter_fields = ['name']
        interfaces = (graphene.relay.Node,)
