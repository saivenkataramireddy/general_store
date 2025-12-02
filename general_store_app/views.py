from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product,Customer,Offer
from django.db.models import Sum, Count


def home(request):
    offers = Offer.objects.filter(is_active=True)
    return render(request, "index.html", {"offers": offers})



def signup(request):
    return render(request,"signup.html")

def login(request):
    return render(request,"login.html")

def category_products(request, category):
    items = Product.objects.filter(category=category)
    return render(request, "products.html", {"products": items, "category": category})

def contact(request):
    return render(request,"contact.html")

def admin_dashboard(request):
    products = Product.objects.all()

    total_products = products.count()
    total_stock_value = products.aggregate(total=Sum('price'))['total'] or 0

    category_data = Product.objects.values('category').annotate(
        count=Count('id')
    )

    total_customers = Customer.objects.count()

    context = {
        'products': products,
        'total_products': total_products,
        'total_stock_value': total_stock_value,
        'category_data': list(category_data),
        'total_customers': total_customers,
    }

    return render(request, "dashboard.html", context)


def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        price = request.POST['price']
        image = request.FILES.get('image')

        Product.objects.create(
            name=name,
            category=category,
            price=price,
            image=image
        )
        return redirect('admin_dashboard')

    context = {
        'categories': Product.CATEGORY_CHOICES,  # ✅ Pass categories here
    }

    return render(request, 'add_product.html', context)

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('admin_dashboard')

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == "POST":
        product.name = request.POST['name']
        product.category = request.POST['category']
        product.price = request.POST['price']

        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        
        product.save()
        return redirect('admin_dashboard')

    return render(request, "edit_product.html", {"product": product, "categories": Product.CATEGORY_CHOICES})
