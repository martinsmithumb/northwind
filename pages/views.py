from django.shortcuts import render
from orders.models import Shipper, Order
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

def shippers(request):
    shippers = Shipper.objects.all()
    orders = Order.objects.all()
    names = []
    for shipper in shippers:
        names.append(str(shipper))

    order_counts = Order.objects.values('ship_via').annotate(num=Count('customer_id')) 

    counts = []
    for item in order_counts:
        counts.append(item['num'])

    context = {
        'shippers': shippers,
        'names': names,
        'counts': counts,
        'orders':  orders,
    }
    return render(request, 'pages/shippers.html', context)

def categories(request):
    shippers = Shipper.objects.all()
    names = []
    for shipper in shippers:
        names.append(str(shipper))

    orders = Order.objects.values('ship_via').annotate(num=Count('customer_id')) 

    counts = []
    for item in orders:
        counts.append(item['num'])

    context = {
        'shippers': shippers,
        'names': names,
        'counts': counts,
    }
    return render(request, 'pages/shippers.html', context)
