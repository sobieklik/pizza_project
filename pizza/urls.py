from django.urls import path, include
from django.conf.urls import url
from . import views

app_name='pizza'

urlpatterns=[
    path('check_cart_len', views.check_cart_len, name='check_cart_len'),
    path('index_payment_successful', views.index_payment_successful, name='index_payment_successful'),
    path('index_payment_successful', views.index_payment_successful, name='index_payment_successful'),
    path('index_payment_cancelled', views.index_payment_cancelled, name='index_payment_cancelled'),
    path('', views.index, name='index'),

]