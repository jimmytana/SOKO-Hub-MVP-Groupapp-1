<<<<<<< HEAD
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
=======
from django.db import models 
from accounts.models import CustomUser
from products.models import Product
class Order (models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total = models.IntegerField()
    status = models.TextField(choices=[('pending', 'Pending'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')])
    delivery_address = models.TextField()
    phone = models.TextField()
    created_at = models.DateTimeField( auto_now_add=True)
>>>>>>> 52ccd12724bef1d2e94201d4145ecc697fe91e40
    def __str__(self):
        return (f"Customer: {self.customer}\nTotal: {self.total}\ndelivery address:{self.delivery_address}")

<<<<<<< HEAD
    

class order_Item(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    price=models.IntegerField()
=======
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
>>>>>>> 52ccd12724bef1d2e94201d4145ecc697fe91e40
    def __str__(self):
        return (f"Order: {self.order}\nproduct: {self.product}\nprice: {self.price}")
