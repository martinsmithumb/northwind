from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .models import Order, Shipper
from rest_framework import viewsets
from .serializers import OrderSerializer, ShipperSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class ShipperViewSet(viewsets.ModelViewSet):
    serializer_class = ShipperSerializer
    queryset = Shipper.objects.all()