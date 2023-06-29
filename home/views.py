from django.shortcuts import render
from products.models import Product, Brand, SliderImage


def home_page(request):
    recently_added_products = Product.objects.order_by('-id')[:4]
    slider_images = SliderImage.objects.all()
    brands = Brand.objects.all()

    context = {
        'products': recently_added_products,
        'slider_images': slider_images,
        'brands': brands
    }
    return render(request, 'home.html', context)
