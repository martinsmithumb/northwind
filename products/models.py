from django.db import models
from django.urls import reverse
from suppliers.models import Supplier


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True, null=False)
    category_name = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=300, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('products:product_list_by_category', args=[self.slug])


class Product(models.Model):    
    product_id = models.IntegerField(primary_key=True, null=False)
    product_name = models.CharField(max_length=200, db_index=True)      
    unit = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    supplier = models.ForeignKey(Supplier, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
 