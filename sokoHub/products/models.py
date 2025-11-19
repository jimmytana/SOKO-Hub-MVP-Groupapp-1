from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    vendor = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/')
    status = models.CharField(max_length=50, default='available')
    created_at = models.DateTimeField(default=timezone.now)