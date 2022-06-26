from django.urls import path
from . import views

urlpatterns = [
    path('producthome', views.producthome, name='producthome'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    
]