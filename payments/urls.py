from django.conf.urls import url
from django.urls import path
from . import views

app_name='payments'

urlpatterns = [
    path('process', views.payment_process, name='payment_process' ),
    path('done', views.payment_done, name='payment_done' ),
    path('cancelled', views.payment_cancelled, name='payment_cancelled' ),

]