from django.shortcuts import render, get_object_or_404, redirect
from orders.models import Order
from shippers.models import Shipper
from suppliers.models import Supplier
from customers.models import Customer
from products.models import Product
from orders.models import Order
from employees.models import Employee
from django.db.models import Count, Avg
from django.contrib import messages, auth
import json
from .data import countries
# import environ

# env = environ.Env()
# env.read_env('./base/.env')

def index(request):
    context = {}    
    return render(request, 'pages/index.html', context)

def logout(request):
    auth.logout(request)
    return render(request, 'pages/index.html')

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

