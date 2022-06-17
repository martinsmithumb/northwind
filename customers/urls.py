from django.urls import path

from . import views

urlpatterns = [
    path('customerhome', views.customerhome, name='customerhome'),
]