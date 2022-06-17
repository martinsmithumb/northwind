from django.urls import path

from . import views

urlpatterns = [
    path('employeehome', views.employeehome, name='employeehome')
]
