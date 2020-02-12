from django.urls import path
from .views import products
from .views import product

app_name='shop'
urlpatterns = [
    path('products/', products, name='products'),
    path('details/', product, name='details'),
]