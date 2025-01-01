from django.contrib import admin
from .models import Product, ProductImage, ChaiVarity, Store, ChaiReview, ChaiCertificate
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

# Register your models here.
class ChaiReviewInline (admin.TabularInline):
  model = ChaiReview
  extra = 2
class ChaiVarietyAdmin (admin.ModelAdmin):
  list_display = ('name', 'type', 'date_added')
  inlines = [ChaiReviewInline]
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')

admin.site.register(ChaiVarity, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
