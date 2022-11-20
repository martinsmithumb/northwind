from django.shortcuts import render, get_object_or_404
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

def shipper(request, shipper_id):
    shipper = get_object_or_404(Shipper, pk=shipper_id)
    context = {
        'shipper': shipper
    }
    return render(request, 'shippers/shipper.html', context)