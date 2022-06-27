from django.shortcuts import render, get_object_or_404
from .models import Customer

def customerhome(request):
    customers = Customer.objects.all()
    context = {
        'customers' : customers ,
    }
    return render(request, 'customers/customerhome.html', context)

def customer(request, customer_id):
  customer = get_object_or_404(Customer, pk=customer_id)

  context = {
    'customer': customer
  }

  return render(request, 'customers/customer.html', context)
