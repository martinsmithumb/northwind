from django.db import models

class Shipper(models.Model):
    shipper_id = models.IntegerField(primary_key=True, null=False) 
    company_name = models.CharField(max_length=40, null=True)
    phone = models.CharField(max_length=24, null=True)
    def __str__(self):
        return self.company_name
