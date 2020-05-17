from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from pizza.models import UUID, Sauce_SIZE
from django.urls import reverse
from cart.cart import Cart
from .forms import OrderForm
from .models import OrderItem, OrderSauce, Order
from django.conf import settings
from django.contrib import messages
from django.views.generic.detail import DetailView
from .tasks import send_sms
import urllib
from decimal import Decimal
import json

def order(request):
    """ Create Order or return OrderForm """

    cart = Cart(request) 
    data = request.session.get('data') 
    dictionary = json.loads(data['dict'])

    if request.method == 'POST':    

        # create form from sent data
        form = OrderForm(request.POST)

        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                # if reCAPTCHA have success status

                order_save = form.save()
                order_save.total_account = cart.get_total_price()
                order_save.save()
                
                for item in cart:
                    # get dictionary from nested dictionary which was created in js

                    selected_item = dictionary.get(item['product_id'])
                    meat = selected_item.get('meat')
                    chips = selected_item.get('chips')
                    sauces = selected_item.get('sauce')

                    chips_result = None
                    meat_result = None
                    total_sauce = 0

                    for i, prod in enumerate(OrderItem.MEAT):
                        if prod[1] in meat :
                            meat_result = prod[0]
                    

                    for i, prod in enumerate(OrderItem.CHIPS):
                        if prod[1] in chips :
                            chips_result=prod[0]
                    
                    order_item = OrderItem.objects.create(order = order_save, product = UUID.objects.get(id=item['product_id']), quantity = item['quantity'], 
                                                        price=item['total_price'], meat = meat_result, chips = chips_result)
                    
                    for key, value in sauces.items(): 
                        # check sauce keys from sent dictionary with name of sauce object
                        # it alert when someone modyfy dictionary sent by js     
                        try:
                            selected_sauce = Sauce_SIZE.objects.get(name=key)
                        except:
                            order_save.delete()
                            return render(request, "order/order.html", {'error' : 'Zamówienie nie zostało zrealizowane. Spróbuj skontaktować się telefonicznie' })
                    
                        total_sauce += int(value)

                        OrderSauce.objects.create(order = order_item, sauce = selected_sauce, quantity = int(value))
                    

                    if total_sauce != int(item['all_sauce']):
                        # check total sauce quantity
                        # it alert when someone modyfy dictionary sent by js 
                        return render(request, "order/order.html", {'error' : 'Zamówienie nie zostało zrealizowane. Spróbuj skontaktować się telefonicznie' })
                    
                cart.clear()

                if order_save.paid_method == 'transfer':
                    
                    request.session['order_id'] = order_save.id
                    return redirect(reverse('payments:payment_process'))

                # asynchronous call sms function
                send_sms.delay(order_save.id) 
                
                return render(request, "order/order_created.html", 
                    {   
                        'order_id' : order_save.id, 
                        'message_1' : "Twoje zamówienie zostało przyjęte.", 
                        'message_2' : "Niebawem ktoś z nim przybędzie." 
                    })
                
            else:
                # if reCAPTCHA have unsuccess status
                return render(request, "order/order.html", {'error' : 'Błąd uwierzytelniania. Spróbuj ponownie' })

    else:
        form = OrderForm()

    return render(request, "order/order.html", {'cart' : cart, 'form' : form, 'filled_form' : dictionary})
