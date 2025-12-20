from django.contrib import admin
<<<<<<< HEAD
from .models import order_Item, Order
# Register your models here.

admin.site.register(order_Item)
=======
from .models import Order, OrderItem
# Register your models here.

admin.site.register(OrderItem)
>>>>>>> 52ccd12724bef1d2e94201d4145ecc697fe91e40
admin.site.register(Order)