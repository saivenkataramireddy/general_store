from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("Milk & Curd", "Milk & Curd"),
        ("Ice Creams", "Ice Creams"),
        ("Daily Groceries", "Daily Groceries"),
        ("Electrical Items", "Electrical Items"),
        ("Home Utility Items", "Home Utility Items"),
        ("Soaps & Detergents", "Soaps & Detergents"),
        ("Snacks & Biscuits", "Snacks & Biscuits"),
        ("Cool Drinks", "Cool Drinks"),
        ("Personal Care", "Personal Care"),
        ("Agricultural Items", "Agricultural Items"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    
    def __str__(self):
        return self.name

class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

