from django.urls import path
from .views import products
from .views import product

app_name='shop'
urlpatterns = [
    path('products/', products, name='shop'),
    path('details/', product, name='shop'),
]