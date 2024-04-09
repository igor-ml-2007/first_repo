from django.contrib import admin
from products.models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'category']

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']
