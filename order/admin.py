from django.contrib import admin
from .models import Order, OrderItem, OrderSauce
import nested_admin


class OrderSauce_Admin(nested_admin.NestedTabularInline):
    model = OrderSauce
    field = '__all__'
   
    extra=0


class OrderItem_Admin(nested_admin.NestedTabularInline):
    model = OrderItem
    inlines = [OrderSauce_Admin,]
    field = '__all__'
    extra=0

@admin.register(Order)
class Order_Admin(nested_admin.NestedModelAdmin):
    
    field = '__all__'
    inlines = [OrderItem_Admin,]
    search_fields = ['full_name', 'phone' ]
    list_display = ['get_id', 'time', 'full_name', 'phone', 'paid_method', 'paid']
    sortable_by = ['get_id', 'time']
    list_filter = ['paid_method', 'paid']

    def get_id(self, object):
        """ returns price of selected pizza's size """
        return object.id      

# Register your models here.
