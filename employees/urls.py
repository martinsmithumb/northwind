from django.urls import path

from . import views

urlpatterns = [
    path('employeehome', views.employeehome, name='employeehome'),
    path('<int:employee_id>/', views.employee, name='employee'),
]
