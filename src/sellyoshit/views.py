from django.shortcuts import render
from .models import Product
from ads.models import Advertisement
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from stats.signals import object_viewed_signal


def products(request):
    products = Advertisement.objects.all().order_by('-created_date')
    paginator = Paginator(products, 6)  # Show X products per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'products': page_obj.object_list,
               'page_obj': page_obj}

    return render(request, 'sellyoshit/product_listEXT.html', context)

def ad(request, pk):
    ad = Product.objects.get(pk=pk)
    context = {'ad': ad}
    return render(request, 'sellyoshit/product_details.html', context)

