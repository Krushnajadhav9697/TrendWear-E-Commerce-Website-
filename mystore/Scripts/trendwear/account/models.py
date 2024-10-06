from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)  # Make optional
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        # return self.full_name
        return self.full_name or str(self.full_name)

