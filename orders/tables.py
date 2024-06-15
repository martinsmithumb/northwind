
import django_tables2 as tables
from .models import Order

class OrderTable(tables.Table):
    class Meta:
        model = Order
        template_name = 'django_tables2/bootstrap.html'
        fields = ("order_id","customer","employee","order_date","required_date","shipped_date","ship_via","freight","ship_name","ship_address","ship_city","ship_region","ship_postal_code","ship_country","slug")
