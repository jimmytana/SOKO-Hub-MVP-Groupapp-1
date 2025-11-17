from django.contrib import admin
from .models import order_Item, Order
# Register your models here.

admin.site.register(order_Item)
admin.site.register(Order)