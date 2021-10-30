from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ['customer_id','company_name','contact_name','contact_title','address','city','region','postal_code','country','phone','fax']
    list_display = ['customer_id','company_name','contact_name','contact_title','address','city','region','postal_code','country','phone','fax']
    list_display_links = ['customer_id']
    list_filter = ['city']
    search_fields = ['company_name']


