from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home(request):
    return render(request,"index.html")


def signup(request):
    return render(request,"signup.html")

def login(request):
    return render(request,"login.html")

def category_products(request, category):
    items = Product.objects.filter(category=category)
    return render(request, "products.html", {"products": items, "category": category})

def contact(request):
    return render(request,"contact.html")