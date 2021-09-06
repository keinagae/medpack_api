import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .types import ProductType


class ProductQuery(graphene.ObjectType):
    products=DjangoFilterConnectionField(ProductType)
