from django.shortcuts import render

from ads.models import Advertisement, Category
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from stats.signals import object_viewed_signal


def products(request):
    """View for showing all ads and paginating them over multiple pages"""
    products = Advertisement.objects.all().filter(sold=False).order_by('-created_date')
    paginator = Paginator(products, 6)  # Show X products per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()

    context = {'products': page_obj.object_list,
               'page_obj': page_obj,
               'categories': categories}

    return render(request, 'sellyoshit/product_listEXT.html', context)


def ad(request, pk):
    """View for showing a specific ad"""
    ad = Advertisement.objects.get(pk=pk)
    context = {'ad': ad}
    return render(request, 'sellyoshit/product_details.html', context)