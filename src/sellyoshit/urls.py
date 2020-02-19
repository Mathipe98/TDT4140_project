from django.urls import path
from .views import products
from .views import ad
from .views import image_test

app_name='shop'
urlpatterns = [
    path('products/', products, name='products'),
    path('details/<int:pk>', ad, name='details'),
    path('Image_test/', image_test, name='image_test'),
]