from django.shortcuts import render
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from order.models import Order
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payment_done(request):
    """ Call when payment was successful """

    order_id = request.session.get('order_id')
    return render(request, 'order/order_created.html',
        {   'order_id' : order_id, 
            'message_1' : "Twoje zamówienie zostało przyjęte.", 
            'message_2' : "Niebawem ktoś z nim przybędzie." 
        })

@csrf_exempt
def payment_cancelled(request):
    """ Call when payment was unsuccessful """

    order_id = request.session.get('order_id')
    return render(request, 'order/order_created.html', 
        {   'order_id' : order_id, 
            'message_1' : "Twoje zamówienie nie zostało przyjęte.", 
            'message_2' : "Wystąpił błąd podczas płatności." 
        })

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()
 
    # create dictionary which will be sent to paypal
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.total_cost().quantize(Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'PLN',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('pizza:index_payment_successful')),
        'cancel_return': 'http://{}{}'.format(host, reverse('pizza:index_payment_cancelled')),
    }
    
    # create button form
    form = PayPalPaymentsForm(initial = paypal_dict)

    return render(request, "order_payment.html", {'order_id': order_id, 'form': form })

