from django.shortcuts import render
from orders.models import Order
from shippers.models import Shipper
from suppliers.models import Supplier
from customers.models import Customer
from products.models import Product
from orders.models import Order
from employees.models import Employee
from django.db.models import Count, Avg
import json
from .data import countries
def index(request):
    context = {}    
    return render(request, 'pages/index.html', context)

def tracker(request):
    customers = Customer.objects.all()
    employees = Employee.objects.all()
    suppliers = Supplier.objects.all()
    shippers = Shipper.objects.all()
    context = {
        'countries': countries,
        'customers': customers,
        'employees': employees,
        'suppliers': suppliers,
        'shippers': shippers,
        }
    return render(request, 'pages/tracker.html', context)


def about(request):
    context = {}
    return render(request, 'pages/about.html', context)
    
def chart(request):
    context = {}
    return render(request, 'pages/chart.html', context)

