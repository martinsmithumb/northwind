from django.db import models
from customers.models import Customer
from employees.models import Employee


class Shipper(models.Model):
    shipper_id = models.IntegerField(null=True) 
    company_name = models.CharField(max_length=40, null=True)
    phone = models.CharField(max_length=24, null=True)
    def __str__(self):
        return self.company_name


class Order(models.Model):
    order_id = models.IntegerField(null=True)
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
    ship_country = models.CharField(max_length=15, null=True)    
    def __str__(self):
        return self.order_id



