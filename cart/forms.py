from django import forms
from pizza.models import Sauce_SIZE
from order.models import OrderItem


class SauceForm(forms.Form):
    """ Form options were taken from Sauce_SIZE object """
    sauce = forms.ModelChoiceField(label=u"Sos", queryset=Sauce_SIZE.objects.all() , empty_label=None)

class MeatForm(forms.Form):
    meat = forms.ChoiceField(label=u"", choices=OrderItem.MEAT)   

class ChipsForm(forms.Form):     
    chips = forms.ChoiceField(label=u"", choices=OrderItem.CHIPS)    
