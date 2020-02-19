from django.shortcuts import render
from .models import Product


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'sellyoshit/product_list.html', context)

def ad(request, pk):
    ad = Product.objects.get(pk=pk)
    context = {'ad': ad}
    return render(request, 'sellyoshit/product_details.html', context)

def home(request):
    return render(request, 'sellyoshit/home_page2.html')

def image_test(request):
    #index_file_path = PROJECT_PATH + '/templates/sellyoshit/Clickable_image_test.html'
    return render(request, "sellyoshit/Clickable_image_test.html")

