from django.db import models

# Create your models here.

class InfoRestaurant(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)