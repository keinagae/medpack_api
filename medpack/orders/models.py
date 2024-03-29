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
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["-id"]


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    quantity=models.IntegerField(default=1)
    product=models.ForeignKey("products.Product",on_delete=models.CASCADE)
