from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Order, Shipper
from rest_framework import viewsets
from .serializers import OrderSerializer, ShipperSerializer
import plotly.express as px
from django_tables2 import SingleTableView
from .tables import OrderTable

class OrderListView(SingleTableView):
    model = Order
    table_class = OrderTable
    template_name = 'orders/ordertable.html'
    
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
    order = get_object_or_404(Order, pk=order_id)
    context = {
        'order': order
    }
    return render(request, 'orders/order.html', context)

# def ordersdash(request):
#     orders = Order.objects.all()
    
#     fig = px.line(
#         x=[o.date for o in orders],
#         y=[o.average for o in orders],
#     )
    
#     chart = fig.to_html()
    
#     context = {'chart':chart}