from django.urls import path

from . import views

urlpatterns = [
    path('supplierhome', views.supplierhome, name='supplierhome'),
]