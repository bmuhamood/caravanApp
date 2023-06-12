from django.urls import path
from .views import index, product_detail
from . import views

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('dashboard/add_caravan/', views.add_caravan, name='add_caravan'),
    path('add_product/', views.add_product, name='add_product'),
]