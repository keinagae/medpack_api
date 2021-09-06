from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from medpack.users.api.views import UserViewSet
from medpack.products.api.views import MyProductViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet,basename="users")
router.register("products/my",MyProductViewSet,basename="products")


app_name = "api"
urlpatterns = router.urls
