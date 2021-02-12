from django.contrib import admin
from .models import Product,Purchase
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','created']


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display= ['product','price','quantity','total_price','salesman']


