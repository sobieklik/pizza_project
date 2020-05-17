from django.urls import path
from django.conf.urls import url
from . import views

app_name='cart'

urlpatterns=[
    path('add/<id>', views.add_item, name='add_item'),
    path('add_item_to_cart/<id>', views.add_item_to_cart, name='add_item_to_cart'),
    path('subtract/<id>', views.subtract_item, name='subtract_item'),
    path('remove/<id>', views.remove_item, name='remove_item'),
    path('add_sauce/<id>', views.add_sauce, name='add_sauce'),
    path('delete_sauce/<id>', views.delete_sauce, name='delete_sauce'),
    path('', views.cart, name='cart'),
] 