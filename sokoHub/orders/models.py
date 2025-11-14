from django.db import models 
from accounts.models import CustomUser
from products.models import Product
class Order (models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total = models.IntegerField()
    status = models.TextField()
    delivery_address = models.TextField()
    phone = models.TextField()
    created_at = models.TimeField( auto_now=False, auto_now_add=False)
    def __str__(self):
        return (f"Customer: {self.customer}\nTotal: {self.total}\ndelivery address:{self.delivery_address}")

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return (f"Order: {self.order}\nproduct: {self.product}\nprice: {self.price}")