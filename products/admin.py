from django.contrib import admin
from .models import Product, Offer, ProductImage, Brand, SliderImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'manufacturer', 'year', 'condition', 'dimensions', 'weight', 'availability')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('get_product_name', 'images')

    def get_product_name(self, obj):
        return obj.product.name

    get_product_name.short_description = 'Product Name'

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')

admin.site.register(SliderImage)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
