from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)  # Show X products per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'products': page_obj.object_list,
               'page_obj': page_obj}

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

