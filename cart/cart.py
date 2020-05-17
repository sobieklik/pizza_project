from decimal import Decimal
from django.conf import settings
from pizza.models import UUID, Sauce, Sauce_SIZE
from cart.forms import SauceForm
from django import template
import logging
logger = logging.getLogger("mylogger")

class Cart(object):

    def __init__(self, request):
        """ Create new cart """

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, request, uuid_object):
        """ Add product to cart or increase its quantity """

        product_id = str(uuid_object.id)

        # Check to what model class belongs UUID
        try:
            product = uuid_object.uuid_Food

            # Check what boolean field was selected and assing this choice to variable
            if product.model.change_meat == True and product.model.change_chips == True:
                type_of_product="food_chips_meat"
            elif product.model.change_meat == True:
                type_of_product="food_meat"
            elif product.model.change_chips == True:
                type_of_product="food_chips"
            else:
                type_of_product="food"
        except:
            pass

        try:
            product = uuid_object.uuid_Pizza
            type_of_product="pizza"
        except:
            pass 

        try:
            product = uuid_object.uuid_Drink
            type_of_product="drink"
        except:
            pass

        if product_id not in self.cart:
            # Create dictionary of each product added to cart
            self.cart[product_id] = { 'product_id': product_id, 'name': product.model.name,'type': type_of_product, 
                                      'size': product.get_size_display(), 'description': product.model.description, 
                                      'price': str(product.price), 'quantity': 1 ,'sauce' : str(product.sauce), 'extra_sauce': 0 }
        else:
            self.cart[product_id]['quantity'] += 1
         
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def subtract(self, uuid_object):
        """ Decrease quantity of product or remove its """

        product_id = str(uuid_object.id)

        if self.cart[product_id]['quantity'] == 1:
            del self.cart[product_id]
        else:
            self.cart[product_id]['quantity'] -= 1
          
        self.save()

    def remove(self, uuid_object):
        """ Remove product from cart """

        product_id = str(uuid_object.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def add_sauce(self, uuid_object):
        """ Increase quantity of product """

        product_id = str(uuid_object.id)
        self.cart[product_id]['extra_sauce'] += 1
        logger.info( self.cart[product_id]['extra_sauce'])
        self.save()

    def delete_sauce(self, uuid_object):
        """ Decrease quantity of product"""

        product_id = str(uuid_object.id)
        self.cart[product_id]['extra_sauce'] -= 1
        logger.info( self.cart[product_id]['extra_sauce'])
        self.save()

    def __iter__(self):
        """ After reload page dictionary is modyfyied """        

        for item in self.cart.values():
            item['all_sauce'] = self.count_sauce(item['product_id'])
            item['total_price'] = self.item_total_price(item['product_id'])
            self.save()
            yield item
            

    def __len__(self):
        """ Returns how many items are in cart """
        return sum(item['quantity'] for item in self.cart.values())

    def count_sauce(self, uuid_object):
        """ Count all sauce assign with product """

        item =  self.cart[uuid_object] 
        return str(int(item['sauce']) * item['quantity'] + item['extra_sauce'])

    def item_total_price(self, uuid_object):
        """ Returns total price of product """

        item =  self.cart[uuid_object]
        return str(Decimal(item['price']) * item['quantity'] + int(item['extra_sauce']) * Sauce.objects.all().first().price)

    def get_total_price(self):
        """ Returns total price of products in cart """

        return sum((Decimal(item['price']) * item['quantity'] + int(item['extra_sauce']) * Sauce.objects.all().first().price) for item in self.cart.values())


    def clear(self):
        """ Delete all products from cart """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True