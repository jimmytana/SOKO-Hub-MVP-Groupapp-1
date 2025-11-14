from django.db import models

# Create your models here.
class CustomUser(models.Model):
    user_type = models.TextField(choices=[('vendor', 'Vendor'), ('customer', 'Customer')])
    phone = models.TextField()
    location = models.TextField()
    def __str__(self):
        return (f"type: {self.user_type}\n phone: {self.phone}\nlocation: {self.location}")
    