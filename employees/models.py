from django.db import models

class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True, null=False) 
    last_name = models.CharField(max_length=20, null=True)
    first_name = models.CharField(max_length=10, null=True)
    title = models.CharField(max_length=30, null=True)
    title_of_courtesy = models.CharField(max_length=25, null=True)
    birth_date =  models.DateField()
    hire_date =  models.DateField()
    address = models.CharField(max_length=60, null=True)
    city = models.CharField(max_length=15, null=True)
    region = models.CharField(max_length=15, null=True)
    postal_code = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=15, null=True)
    home_phone = models.CharField(max_length=24, null=True)
    extension = models.CharField(max_length=4, null=True)
    photo = models.CharField(max_length=10, null=True)
    notes = models.CharField(max_length=200, null=True)
    reports_to = models.IntegerField(null = True)
    photo_path = models.CharField(max_length=255, null=True)
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
