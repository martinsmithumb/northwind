from django.urls import path

from . import views

urlpatterns = [
    path('shipperhome', views.shipperhome, name='shipperhome'),
    path('shipperold', views.shipperold, name='shipperold'),
    path('ship_populator', views.ship_populator, name='ship_populator'),
]