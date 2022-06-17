from django.shortcuts import render
from .models import Shipper
from orders.models import Order
from django.db.models import Count

def shipperhome(request):
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
    return render(request, 'shippers/shipperhome.html', context)

def shipperold(request):
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
    return render(request, 'shippers/shipperold.html', context)


def ship_populator(request):
    shippers = Shipper.objects.all()
    shipper_ids = []
    company_names = []
    
    for shipper in shippers:
        company_names.append(str(shipper))
        shipper_ids.append(str(shipper.shipper_id))

    context = {
        'shippers': shippers,
        'company_names': company_names,
        'shipper_ids':shipper_ids,
    }
    return render(request, 'shippers/ship_populator.html', context)