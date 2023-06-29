from django.urls import path
from .views import index, product_detail
from . import views

app_name = 'products'

urlpatterns = [
    path('products/', views.index, name='index'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
]