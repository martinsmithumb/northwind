from django.db import models

class Supplier(models.Model):
    supplier_id = models.IntegerField(primary_key=True, null=False) 
    supplier_name = models.CharField(max_length=200, null=True)
    contact_name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=40, null=True)
    zip = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=24, null=True)
    def __str__(self):
        return self.supplier_name

