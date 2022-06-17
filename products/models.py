from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True, null=False)
    category_name = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=300, db_index=True)



class Product(models.Model):    
    product_id = models.IntegerField(primary_key=True, null=False)
    product_name = models.CharField(max_length=200, db_index=True)
    supplier_id = models.SlugField(max_length=200, db_index=True)
    category_id = models.TextField(blank=True)
    unit = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 