from django.urls import path
from .views import products
from .views import product
from .views import image_test

app_name='shop'
urlpatterns = [
    path('products/', products, name='products'),
    path('details/', product, name='details'),
    path('Image_test/', image_test, name='image_test'),
]