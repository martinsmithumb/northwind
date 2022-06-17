from django.urls import path, include
from . import views
from rest_framework import routers
from .views import OrderViewSet, ShipperViewSet


router = routers.DefaultRouter()
router.register('api/orders', OrderViewSet)
router.register('api/shippers', ShipperViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orderhome', views.orderhome, name='orderhome')
]
