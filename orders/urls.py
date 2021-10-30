from django.urls import path, include
from . import views
from rest_framework import routers
from .views import OrderViewSet, ShipperViewSet


router = routers.DefaultRouter()
router.register('orders', OrderViewSet)
router.register('shipper', ShipperViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
