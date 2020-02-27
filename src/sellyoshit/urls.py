from django.conf.urls import url
from django.urls import path
from .views import products
from .views import ad

app_name='shop'
urlpatterns = [
    path('products/', products, name='products'),
    path('details/<int:pk>', ad, name='details'),
]