from django.contrib.auth import get_user_model
from django.db import models


class WithTimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class WithCreator(models.Model):
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True
