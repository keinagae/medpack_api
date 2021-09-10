from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class BagPackStatus(models.TextChoices):
    ACTIVE=("active",'Active')
    CANCELED=("canceled",'Canceled')
    ORDERED=("ordered",'Ordered')

class BagPack(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    status=models.CharField(max_length=30,default=BagPackStatus.ACTIVE,choices=BagPackStatus.choices)


class BagPackItem(models.Model):
    bagpack=models.ForeignKey(BagPack,on_delete=models.CASCADE,related_name="items")
    product=models.ForeignKey("products.Product",on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
