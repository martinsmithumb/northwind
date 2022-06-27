from django.urls import path
from . import views

urlpatterns = [
    path('producthome', views.producthome, name='producthome'),
    path('<int:product_id>/', views.product, name='product'),
]