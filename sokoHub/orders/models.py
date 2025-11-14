from django.db import models

# Create your models here.
class order(models.Model):
    customer=models.Foreignkey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    total=models.DecimalFields()
    status=models.charFields()
    delivery_adress=models.charFields(max_length=200)
    phone=models.integerFields()
    created_at=models.DatetimeField(auto_now_add=True)
    def __str__(self):
         return f"Order {self.order_number} — {self.customer.username}"
           

    

class order_Item(models.Model):
    order=models.Foreignkey(order,on_delete=models.CASCADE)
    product=models.ForeinKey(on_delete=models.CASCADE)
    Quantity=models.DecimalFields()
    price=models.DecimalFields()
    def __str__(self):
     return f"{self.product} x {self.quantity}"

    

