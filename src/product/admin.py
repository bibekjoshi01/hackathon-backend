from django.contrib import admin

from .models import Product, ProductCategory, ProductImage

admin.site.register(ProductImage)
admin.site.register(Product)
admin.site.register(ProductCategory)
