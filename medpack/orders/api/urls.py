from django.urls import path

from medpack.orders.api.views import OrderListApiView,OrderCreateApiView

urlpatterns=[
    path("",OrderListApiView.as_view()),
    path('add',OrderCreateApiView.as_view())
]
