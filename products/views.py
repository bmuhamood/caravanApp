# from django.shortcuts import render, get_object_or_404
# from .models import Product
#
# def index(request):
#     products = Product.objects.all()
#     return render(request, 'index.html', {'products': products})
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'product_detail.html', {'product': product})

from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # Get the list of recently viewed items from the session
    recently_viewed = request.session.get('recently_viewed', [])

    # Add the current product to the recently viewed list
    if pk not in recently_viewed:
        recently_viewed.append(pk)

    # Limit the recently viewed list to a certain number of items (e.g., 5)
    if len(recently_viewed) > 5:
        recently_viewed = recently_viewed[-5:]

    # Update the session with the recently viewed list
    request.session['recently_viewed'] = recently_viewed

    # Retrieve the recently viewed products
    recently_viewed_products = Product.objects.filter(pk__in=recently_viewed)

    return render(request, 'product_detail.html', {'product': product, 'recently_viewed_products': recently_viewed_products})
