from django.urls import path
from . import views

urlpatterns = [
    path('shipperhome', views.shipperhome, name='shipperhome'),
    path('ship_populator', views.ship_populator, name='ship_populator'),
    path('<int:shipper_id>/', views.shipper, name='shipper'),
]