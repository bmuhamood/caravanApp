from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def add_caravan(request):
    # Add your logic here
    return render(request, 'add_caravan.html')

def add_product(request):
    # Add your view logic here
    return render(request, 'add_caravan.html')