from django.shortcuts import render
from products.models import Product

def home_page(request):
    recently_added_products = Product.objects.order_by('-id')[:6]
    context = {'products': recently_added_products}
    return render(request, 'home.html', context)

