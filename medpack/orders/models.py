from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class OrderStatus(models.TextChoices):
    PENDING=("pending","Pending")
    APPROVED=("approved","Approved")
    COMPLETED=("completed","Completed")
    CANCELED=('canceled',"Canceled")


class Order(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    status=models.CharField(max_length=30,default=OrderStatus.PENDING,choices=OrderStatus.choices)


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    product=models.ForeignKey("products.Product",on_delete=models.CASCADE)
