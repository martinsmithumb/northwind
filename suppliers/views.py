from django.shortcuts import render
from .models import Supplier

def supplierhome(request):
    suppliers = Supplier.objects.all()



    context = {
        'suppliers': suppliers,
    }
    return render(request, 'suppliers/supplierhome.html', context)