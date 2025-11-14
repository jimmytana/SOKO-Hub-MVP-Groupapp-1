from django.db import models

# Create your models here.
class Product(models.Model):
    vendor = models.IntegerField(models.ForeignKey("accounts.Model", on_delete=models.CASCADE))
    name = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='')
    status = models.TextField()
    created_at = models.TimeField()
    