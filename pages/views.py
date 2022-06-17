from django.shortcuts import render
from orders.models import Order
from shippers.models import Shipper
from django.db.models import Count
import json

def index(request):
    context = {}
    return render(request, 'pages/index.html', context)


def about(request):
    context = {}
    return render(request, 'pages/about.html', context)
    
def chart(request):
    context = {}
    return render(request, 'pages/chart.html', context)

