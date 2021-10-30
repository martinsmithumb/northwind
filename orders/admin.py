from django.contrib import admin
from .models import Shipper, Order


@admin.register(Shipper)
class ShipperAdmin(admin.ModelAdmin):
    fields = ['shipper_id','company_name','phone']
    list_display = ['shipper_id','company_name','phone']
    list_display_links = ['company_name']
    list_filter = ['company_name']
    search_fields = ['company_name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['ship_name','order_date','required_date','shipped_date','freight', 'ship_name','ship_address','ship_city','ship_region','ship_postal_code','ship_country','ship_via','customer_id']    
    list_filter = ['ship_via']
    list_per_page = 25
