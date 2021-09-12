from enum import Enum
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

from medpack.utils.models import WithTimeStamps



class ProductStatusEnum(models.TextChoices):
    PENDING = "pending", "Pending"
    APPROVED = "approved", "Approved"
    EXPIRED = "expired","Expired",
    OUT_OF_STOCK="out_of_stock","Out Of Stock"


class Product(WithTimeStamps, models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    expiry_date = models.DateField()
    quantity = models.IntegerField(default=1)
    provider = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(max_length=30, default=ProductStatusEnum.PENDING, choices=ProductStatusEnum.choices)


class Variant(WithTimeStamps, models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)


class VariantAttribute(WithTimeStamps, models.Model):
    variant = models.ForeignKey("Variant", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class VariantAttributeValues(WithTimeStamps, models.Model):
    attribute = models.ForeignKey("VariantAttribute", on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
