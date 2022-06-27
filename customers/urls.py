from django.urls import path

from . import views

urlpatterns = [
    path('customerhome', views.customerhome, name='customerhome'),
    path('<str:customer_id>', views.customer, name='customer'),
]