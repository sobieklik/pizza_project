from django.urls import path, include
from django.conf.urls import url
from . import views

app_name='order'

urlpatterns=[
    path('', views.order, name='order'),
    
]

