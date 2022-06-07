from rest_framework import serializers
from .models import Order, Shipper


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # This is where you decide what should be included in the object sent to front end
        fields = ['order_id', 'customer', 'employee', 'order_date', 'required_date', 'shipped_date', 'ship_via', 'freight', 'ship_name', 'ship_address',
         'ship_city', 'ship_region', 'ship_postal_code', 'ship_country']


class ShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipper
        # This is where you decide what should be included in the object sent to front end
        fields = '__all__'






