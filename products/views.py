from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def producthome(request):
    products = Product.objects.all()
    context = {
        'products': products
    }    
    return render(request, 'products/producthome.html', context)
