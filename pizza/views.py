from django.shortcuts import render
from .models import Pizza, Food, Drink
from cart.cart import Cart
from django.http import JsonResponse

def index(request):

    context={
        'pizza_list': Pizza.objects.all().order_by('number'),
        'casserole_list': Food.objects.filter(category='CASSEROLES'),
        'pasta_list': Food.objects.filter(category='PASTAS'),
        'dinner_list': Food.objects.filter(category='DINNERS'),
        'pancake_list': Food.objects.filter(category='PANCAKES'),
        'soup_list': Food.objects.filter(category='SOUPS'),
        'salad_list': Food.objects.filter(category='SALADS'),
        'snack_list': Food.objects.filter(category='SNACKS'),
        'kebab_list': Food .objects.filter(category='KEBAB'),
        'fastfood_list': Food.objects.filter(category='FASTFOODS'),

    }
    return render(request, 'pizza/index.html', context)

def index_payment_successful(request):
    """ Using for display modal which contain info about payment process """

    return render(request, 'pizza/index.html', {'payment': True })

def index_payment_cancelled(request):
    """ Using for display modal which contain info about payment process """

    return render(request, 'pizza/index.html', {'payment': False })


def check_cart_len(request):
    """ Check how many items are in cart """

    cart = Cart(request)
    data = {
        'cart_len': len(cart)
    }
    return JsonResponse(data)