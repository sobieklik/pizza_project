from django.db import models
from django.core.validators import MaxValueValidator
from pizza.models import UUID, Sauce_SIZE
from django.urls import reverse
from django.conf import settings
from decimal import Decimal


class Order(models.Model):

        METHOD = [
                ('cash', 'Gotówka'),
                ('card_payment', 'Płatność kartą'),
                ('transfer', 'Zapłać przez Internet')
                ]

        time = models.DateTimeField(verbose_name=u"Data zamówienia", auto_now_add=True)
        total_account = models.DecimalField(verbose_name=u"Do zapłaty", max_digits=8, decimal_places=2, default=0.00)
        full_name = models.CharField(verbose_name=u"Imię i nazwisko", max_length=100) 
        city = models.CharField(verbose_name=u"Miejscowość", max_length=40)
        street = models.CharField(verbose_name=u"Ulica", max_length=40)
        number_of_house = models.CharField(verbose_name=u"Numer domu / numer mieszkania", max_length=40)
        phone = models.IntegerField(verbose_name=u"Numer kontaktowy", validators=[MaxValueValidator(999999999)])
        paid=models.BooleanField(verbose_name=u"Zamówienie opłacono", default=False)  
        paid_method=models.CharField(verbose_name=u"Metoda płatności", max_length=20, choices=METHOD)
       
        def total_cost(self):
               return self.total_account

class OrderItem(models.Model):

    CHIPS = [
            ('chips', 'Frytki'),
            ('slices', 'Talarki'),
            ('wedges', 'Łódeczki'),
            ('potato', 'Ziemniaki'),
    ]

    MEAT = [
            ('chicken', 'Kurczak'),
            ('veal', 'Cielęcina'),
            ('mix', 'Mix'),
    ]
            

    order=models.ForeignKey(Order, related_name='order_cart', on_delete=models.CASCADE)
    product=models.ForeignKey(UUID, related_name='order_item', on_delete=models.CASCADE)
    price=models.DecimalField(verbose_name=u'Cena', max_digits=5, decimal_places=2)
    meat=models.CharField(verbose_name=u'Mięso', max_length=20, choices=MEAT, blank=True, null=True)
    chips=models.CharField(verbose_name=u'Frytki', max_length=20, choices=CHIPS, blank=True, null=True)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return str(self.order.id)
    
class OrderSauce(models.Model):

    sauce=models.ForeignKey(Sauce_SIZE, related_name='order_sauce', on_delete=models.CASCADE)
    order=models.ForeignKey(OrderItem, related_name='order_sauce', on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return str(self.sauce.name)


