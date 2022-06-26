from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def producthome(request):
    products = Product.objects.all()
    context = {
        'products': products
    }    
    return render(request, 'products/producthome.html', context)

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    return render(request,
                  'products/list.html',
                  {'category': category,
                   'categories': categories})