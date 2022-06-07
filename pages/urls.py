from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('chart', views.chart, name='chart'),
    path('shippers', views.shippers, name='shippers'),
    path('categories', views.categories, name='categories'),
    path('ship_populator', views.ship_populator, name='ship_populator'),
]
