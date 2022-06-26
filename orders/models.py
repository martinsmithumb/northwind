from django.db import models
from django.db.models.functions import Concat
from django.db.models import Value, CharField
from customers.models import Customer
from employees.models import Employee
from shippers.models import Shipper
from products.models import Product
from django.urls import reverse
from django.utils.text import slugify


class OrderManager(models.Manager):
    def get_queryset(self):
        """Overrides the models.Manager method to concatenate strings to the beginning and end of order_id field when the table is queried"""
        qs = super(OrderManager, self).get_queryset()\
            .annotate(link=Concat(Value("<a href='#'>"), 'order_id', Value('</a>'), output_field=CharField()))
        return qs

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, null=True)
    order_date = models.DateField(null=True) 
    required_date = models.DateField(null=True) 
    shipped_date = models.DateField(null=True) 
    ship_via = models.ForeignKey(Shipper, on_delete=models.DO_NOTHING, null=True)
    freight = models.CharField(max_length=24, null=True)
    ship_name = models.CharField(max_length=40, null=True)
    ship_address = models.CharField(max_length=60, null=True)
    ship_city = models.CharField(max_length=15, null=True)
    ship_region = models.CharField(max_length=15, null=True)
    ship_postal_code = models.CharField(max_length=10, null=True)
    ship_country = models.CharField(max_length=15, null=True, blank=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    
    objects = OrderManager()    
    
    # Sorting by order id
    class Meta:
        ordering = ('order_id',)
    


class Order_line(models.Model):
    line = models.IntegerField(primary_key=True, null=False)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, null=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True)
    quantity = models.IntegerField()

