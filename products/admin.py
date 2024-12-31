from django.contrib import admin
from .models import Product, ProductImage
# Register your models here.



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'price')
    search_fields = ['name']
    list_filter = ['price']
    list_editable = ['price']
    list_per_page = 10


