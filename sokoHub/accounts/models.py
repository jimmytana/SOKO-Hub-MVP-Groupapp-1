from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    user_type = models.TextField(choices=[('vendor', 'Vendor'), ('customer', 'Customer')])
    phone = models.TextField()
    location = models.TextField()
    def __str__(self):
        return (f"type: {self.user_type}, phone: {self.phone},location: {self.location}")
