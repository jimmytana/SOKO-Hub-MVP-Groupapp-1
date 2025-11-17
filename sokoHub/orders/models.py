from django.db import models
from products.models import Product
from accounts.models import CustomUser

# Create your models here.
class Order(models.Model):
    customer= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total=models.FloatField()
    status=models.CharField()
    delivery_adress=models.CharField(max_length=200)
    phone=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return f"Order {self.order_number} — {self.customer.username}"
           

    

class order_Item(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    price=models.IntegerField()
    def __str__(self):
     return f"{self.product} x {self.quantity}"

    

