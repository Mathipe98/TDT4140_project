from django.shortcuts import render
from .models import Product


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'sellyoshit/product_list.html', context)

def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'sellyoshit/product_list.html', context)

def home(request):
    return render(request, 'sellyoshit/home_page.html')

def image_test(request):
    #index_file_path = PROJECT_PATH + '/templates/sellyoshit/Clickable_image_test.html'
    return render(request, "sellyoshit/Clickable_image_test.html")