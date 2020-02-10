from django.urls import path
from .views import products

app_name='shop'
urlpatterns = [
    path('products/', products, name='shop'),
]