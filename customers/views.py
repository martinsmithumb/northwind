from django.shortcuts import render
from .models import Customer

def customerhome(request):
    customers = Customer.objects.all()
    context = {
        'customers' : customers ,
    }
    return render(request, 'customers/customerhome.html', context)