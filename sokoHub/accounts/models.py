from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    user_type = models.TextField(choices=[('vendor', 'Vendor'), ('customer', 'Customer')])
    phone = models.TextField()
    location = models.TextField()
    def __str__(self):
<<<<<<< HEAD
        return (f"type: {self.user_type}\n phone: {self.phone}\nlocation: {self.location}")
=======
        return (f"type: {self.user_type}, phone: {self.phone},location: {self.location}")
>>>>>>> 52ccd12724bef1d2e94201d4145ecc697fe91e40
