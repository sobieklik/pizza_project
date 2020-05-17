from django.contrib import admin
from .models import Pizza, Pizza_SIZE, Food, Food_SIZE, Drink, Drink_SIZE, Sauce, Sauce_SIZE, Additives, Additives_SIZE
from django.utils.html import mark_safe

class Pizza_SIZE_Admin(admin.StackedInline):

    model=Pizza_SIZE
    fields=['size', 'sauce', 'price']
    max_num=4
    extra=0

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):

    inlines=[Pizza_SIZE_Admin,]
    search_fields=['pk', 'name' ]
    list_display=[ 'number', 'name', 'description','price_of_SMALL', 'price_of_BIG','price_of_MEGA', 'price_of_GIGA']
    list_filter=['name']
    fieldsets=[('',{'fields':['number', 'name', 'description']}),]
    sortable_by=['number', 'name']
  
    def price_of_SMALL(self, object):
        """ returns price of selected pizza's size """
        return object.pizza_product.filter(size='SMALL').get().price           
    price_of_SMALL.short_description=u"MAŁA [zł]"  

    def price_of_BIG(self, object):
        return object.pizza_product.filter(size='BIG').get().price
    price_of_BIG.short_description=u"DUŻA [zł]"

    def price_of_MEGA(self, object):
        return object.pizza_product.filter(size='MEGA').get().price           
    price_of_MEGA.short_description=u"MEGA [zł] "            
    
    def price_of_GIGA(self, object):
        return object.pizza_product.filter(size='GIGA').get().price           
    price_of_GIGA.short_description=u"GIGA [zł]"            
    
    class Media:
        js = ('js/jquery-3.4.1.min.js',
              'js/pizza-admin.js',
              )
        css = {
            "all": ("css/admin.css",)
        }


class Sauce_SIZE_Admin(admin.StackedInline):

    model = Sauce_SIZE
    fields = ['name']    
    extra = 0

@admin.register(Sauce)
class SauceAdmin(admin.ModelAdmin):

    def product_name(self, object):
        """ allows display name of product using list """

        to_return = '<ul class="item">'
        to_return += '\n'.join('<li>{}</li>'.format(sauce.name)  for sauce in object.sauce_product.all())
        to_return += '</ul>'
        return mark_safe(to_return) 

    product_name.short_description="Sosy"
  
    inlines = [Sauce_SIZE_Admin,]
    list_display=['price', 'product_name']

    fields= ['price']

class Additives_SIZE_Admin(admin.StackedInline):

    model = Additives_SIZE
    fields = ['size', 'price']    
    extra = 0
    max_num=4

@admin.register(Additives)
class AdditivesAdmin(admin.ModelAdmin):

    def price_of_SMALL(self, object):
        return object.additives_product.filter(size='SMALL').get().price           
    price_of_SMALL.short_description=u"MAŁA [zł]"  

    def price_of_BIG(self, object):
        return object.additives_product.filter(size='BIG').get().price
    price_of_BIG.short_description=u"DUŻA [zł]"

    def price_of_MEGA(self, object):
        return object.additives_product.filter(size='MEGA').get().price           
    price_of_MEGA.short_description=u"MEGA [zł] "            
    
    def price_of_GIGA(self, object):
        return object.additives_product.filter(size='GIGA').get().price           
    price_of_GIGA.short_description=u"GIGA [zł]"            
  
    inlines = [Additives_SIZE_Admin,]
    search_fields=[ 'name' ]
    list_display=[ 'name', 'price_of_SMALL', 'price_of_BIG','price_of_MEGA', 'price_of_GIGA']
    fields=['name']
    sortable_by=['name']

    class Media:

        js = ('js/jquery-3.4.1.min.js',
              'js/additives-admin.js',
              )
        css = {
            "all": ("css/admin.css",)
        }


class Food_SIZE_Admin(admin.StackedInline):

    model=Food_SIZE
    fields=['size', 'price', 'sauce']
    extra=0
    max_num=2

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):

    inlines=[Food_SIZE_Admin,]
    search_fields=['name']
    list_display=['name', 'get_category', 'description','price_of_SMALL', 'price_of_BIG', 'change_meat', 'change_chips']   
    fields = ['name', 'category', 'description','change_meat', 'change_chips']      
    list_filter=['category']
    sortable_by=['category','change_meat', 'change_chips']

    def get_category(self, object):
        """ return category of product """

        return object.get_category_display()
    get_category.short_description = 'Kategoria'
    
    def price_of_BIG(self, object):
        return object.food_product.filter(size='BIG').get().price
    price_of_BIG.short_description=u"DUŻA [zł]"

    def price_of_SMALL(self, object):
        return object.food_product.filter(size='SMALL').get().price           
    price_of_SMALL.short_description=u"MAŁA [zł]"

    class Media:
        js = ('js/jquery-3.4.1.min.js',
              'js/food-admin.js',
              )
        css = {
            "all": ("css/admin.css",)
        }


class Drink_SIZE_Admin(admin.TabularInline):
   
    model=Drink_SIZE
    fieldsets= (
                (None, {'fields': ('capacity', ),
                        'classes':('drink',)}),
                (None, {'fields': ('price',)})
    )
    
    extra=0
    
    

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):

    inlines=[Drink_SIZE_Admin,]               
    fields=['name']              
    list_display=['name', 'product_capacity', 'product_price']
    search_fields=['name']

    def change_dot(self, objects):
        """ replace dot with comma """

        return str(objects).replace('.',',') 
     
    def product_capacity(self, object):
      
        to_return = '<ul class="item">'
        to_return += '\n'.join('<li>{}</li>'.format(drink.capacity)  for drink in object.drink_product.all())
        to_return += '</ul>'
        return mark_safe(to_return) 

    product_capacity.short_description="Pojemność [ml]"
  

    def product_price(self, object):
      
        to_return = '<ul class="item">'
        to_return += '\n'.join('<li>{}</li>'.format(self.change_dot(drink.price))  for drink in object.drink_product.all())
        to_return += '</ul>'
        return mark_safe(to_return) 

    product_price.short_description="Cena"




