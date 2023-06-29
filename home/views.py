from django.shortcuts import render
from products.models import Product, Brand

def home_page(request):
    recently_added_products = Product.objects.order_by('-id')[:4]
    context = {'products': recently_added_products}
    return render(request, 'home.html', context)

def home_view(request):
    brands = Brand.objects.all()
    return render(request, 'home.html', {'brands': brands})