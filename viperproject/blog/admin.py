from django.contrib import admin
from .models import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')

admin.site.register(Products, ProductsAdmin)
