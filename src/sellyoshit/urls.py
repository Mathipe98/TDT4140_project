from django.urls import path, include
from .views import products, ad

app_name = 'shop'

"""These urlpatterns are used for testing purposes. Deleting them will cause errors in the test."""
urlpatterns = [
    path('products/', products, name='products'),
    path('details/<int:pk>', ad, name='details'),
]