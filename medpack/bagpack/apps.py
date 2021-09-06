from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class BagpackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'medpack.bagpack'
    verbose_name = _("BagPack")
