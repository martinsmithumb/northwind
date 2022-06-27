from django.shortcuts import render, get_object_or_404
from .models import Supplier

def supplierhome(request):
    suppliers = Supplier.objects.all()



    context = {
        'suppliers': suppliers,
    }
    return render(request, 'suppliers/supplierhome.html', context)

def supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, pk=supplier_id)
    context = {
        'supplier': supplier
    }
    return render(request, 'suppliers/supplier.html', context)