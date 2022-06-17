from socket import fromshare
from django import forms
from localflavor.us.forms import USZipCodeField
from .models import Order

class OrderCreateForm(forms.ModelForm):
    postal_code = USZipCodeField()
    
    class Meta:
        model = Order
        fields = ['customer','employee','order_date','required_date','freight','ship_name'
                  , 'ship_address']