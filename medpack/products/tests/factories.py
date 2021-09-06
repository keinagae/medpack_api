import factory
from medpack.products.models import Product

class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Product %03d" % n)

    class Meta:
        model=Product
