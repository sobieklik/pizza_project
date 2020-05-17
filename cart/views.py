from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_POST
from pizza.models import UUID, Sauce_SIZE
from .cart import Cart
from .forms import SauceForm, ChipsForm, MeatForm
from order.forms import OrderForm
from django.urls import reverse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import json

@require_POST
def add_item(request, id):
    """ 
        Add product to cart using sent uuid.
        Function redirect to main page.
    """
    cart = Cart(request)
    uuid_object = get_object_or_404(UUID, id=id)
    cart.add(request, uuid_object)
    return redirect('pizza:index')

@require_POST
def add_item_to_cart(request, id):
    """ 
        Add product to cart using sent uuid 
    """
    cart = Cart(request)
    uuid_object = get_object_or_404(UUID, id=id)
    cart.add(request, uuid_object)
    return redirect('cart:cart')

@require_POST
def remove_item(request, id):
    """ 
        Decrease quantity of product 
    """
    cart = Cart(request)
    uuid_object = get_object_or_404(UUID, id=id)
    cart.remove(uuid_object)
    return redirect('cart:cart')

@require_POST
def subtract_item(request, id):
    """ 
        Remove product from cart using sent uuid 
    """
    cart = Cart(request)
    uuid_object = get_object_or_404(UUID, id=id)
    cart.subtract(uuid_object)
    return redirect('cart:cart')

@require_POST
def add_sauce(request, id):
    """ 
        Add product to cart using sent uuid 
    """
    cart = Cart(request)
    uuid_object = get_object_or_404(UUID, id=id)
    cart.add_sauce(uuid_object)
    return redirect('cart:cart')

@require_POST
def delete_sauce(request, id):
    """ 
        Remove product from cart using sent uuid 
    """
    cart = Cart(request)
    uuid_object = get_object_or_404(UUID, id=id)
    cart.delete_sauce(uuid_object)
    return redirect('cart:cart')


def cart(request):
    cart = Cart(request)
    if request.method == 'POST' :  
        
        order = OrderForm()
        request.session['data']=request.POST
        return redirect('order:order')

    else:
        form_sauce=SauceForm()
        form_chips=ChipsForm()
        form_meat=MeatForm()
    return render(request, 'cart/cart.html', {'cart': cart, 'form_sauce' : form_sauce, 'form_chips':form_chips, 'form_meat': form_meat })

