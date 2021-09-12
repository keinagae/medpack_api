from typing import Optional, Iterable

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField,EmailField,Model,OneToOneField,CASCADE,ImageField,BooleanField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for medpack."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email=EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class UserProfile(Model):
    user=OneToOneField("User",on_delete=CASCADE,related_name="profile")
    address=CharField(max_length=255,null=True)
    phone=CharField(max_length=30,null=True)
    image=ImageField(null=True,blank=True)
    is_completed=BooleanField(default=False)

    def save(self,**kwargs) -> None:
        if self.address and self.phone:
            self.is_completed=True
        super(UserProfile, self).save(**kwargs)


@receiver(post_save, sender=User, dispatch_uid="user_created")
def update_stock(sender, instance, **kwargs):
    created=kwargs['created']
    if created:
        UserProfile.objects.create(user=instance)
