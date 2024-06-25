# shopping/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    mobile_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
