from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Order, Shipper
from rest_framework import viewsets
from .serializers import OrderSerializer, ShipperSerializer
import plotly.express as px


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class ShipperViewSet(viewsets.ModelViewSet):
    serializer_class = ShipperSerializer
    queryset = Shipper.objects.all()

def orderhome(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'orders/orderhome.html', context)

def order(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    return render(request, 'orders/order.html', {'order': order})

# def ordersdash(request):
#     orders = Order.objects.all()
    
#     fig = px.line(
#         x=[o.date for o in orders],
#         y=[o.average for o in orders],
#     )
    
#     chart = fig.to_html()
    
#     context = {'chart':chart}