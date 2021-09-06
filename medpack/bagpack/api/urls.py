from django.urls import path

from medpack.bagpack.api.views import CartApiView, ItemToCartApiView

urlpatterns=[
    path("",CartApiView.as_view()),
    path('add',ItemToCartApiView.as_view())
]
