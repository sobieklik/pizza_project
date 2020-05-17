from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from order.models import Order


def payment_notification(sender, **kwargs):
    """  After payment check for signal about status payment"""
    ipn_obj = sender
    
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # payment was successful
        order = get_object_or_404(Order, id=ipn_obj.invoice)
        # mark the order as paid
        order.paid = True
        order.save()
        #asynchronous call sms function
        send_sms.delay(order_save.id) 
       
valid_ipn_received.connect(payment_notification)