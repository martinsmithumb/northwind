from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def producthome(request):
    products = Product.objects.all()
    context = {
        'products': products
    }    
    return render(request, 'products/producthome.html', context)
    
def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'products/product.html', context)