from django.conf.urls import url
from django.urls import path
from .views import products
from .views import product
from .views import login


app_name='shop'
urlpatterns = [
    path('products/', products, name='products'),
    path('details/', product, name='details'),
]