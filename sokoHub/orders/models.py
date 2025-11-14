from django.db import models

# Create your models here.
class order(models.Model):
    customer= models.ForeignKey("accounts.Model", on_delete=models.CASCADE)
    total=models.DecimalField()
    status=models.CharField()
    delivery_adress=models.CharField(max_length=200)
    phone=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return f"Order {self.order_number} — {self.customer.username}"
           

    

class order_Item(models.Model):
    order=models.ForeignKey(order,on_delete=models.CASCADE)
    product=models.ForeignKey(on_delete=models.CASCADE)
    Quantity=models.DecimalField()
    price=models.DecimalField()
    def __str__(self):
     return f"{self.product} x {self.quantity}"

    

