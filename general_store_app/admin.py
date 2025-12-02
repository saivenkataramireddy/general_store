from django.contrib import admin
from .models import Product, Customer,Offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Offer)
