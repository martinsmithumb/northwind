from django.db import models

class Customer(models.Model):
    customer_id = models.CharField(max_length=5, primary_key=True, null=False)
    company_name = models.CharField(max_length=40, null=True)
    contact_name = models.CharField(max_length=30, null=True)
    contact_title = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=60, null=True)
    city = models.CharField(max_length=15, null=True)
    region = models.CharField(max_length=15, null=True)
    postal_code = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=15, null=True)
    phone = models.CharField(max_length=24, null=True)
    fax = models.CharField(max_length=24, null=True)
    def __str__(self):
        return self.company_name
