from order.models import Order
from django import forms

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields=['full_name', 'street','number_of_house', 'city', 'phone', 'paid_method']