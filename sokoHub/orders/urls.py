from django.urls import path 
from .views import checkout, placeOrder, myOrders, vendorOrders

urlpatterns = [
    path('checkout', checkout, name='checkout'),
    path('placeOrder', placeOrder, name='placeOrder'),
    path('myOrders', myOrders, name='myOrders'),
    path('orders', vendorOrders, name='orders')
]