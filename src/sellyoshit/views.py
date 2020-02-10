from django.shortcuts import render
from .models import Product


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'sellyoshit/product_list.html', context)

def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'sellyoshit/product_details.html', context)

def home(request):
    home = "hei"
    context = {'home': home}
    return render(request, 'sellyoshit/home_page.html', context)