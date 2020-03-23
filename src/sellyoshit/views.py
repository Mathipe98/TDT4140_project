from django.core.paginator import Paginator
from django.shortcuts import render

from ads.models import Advertisement, Category

"""View for showing all ads and paginating them over multiple pages"""
def products(request):
    products = Advertisement.objects.all().filter(sold=False).order_by('-created_date')
    paginator = Paginator(products, 6)  # Show X products per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()

    context = {'products': page_obj.object_list,
               'page_obj': page_obj,
               'categories': categories}

    return render(request, 'sellyoshit/product_listEXT.html', context)

"""View for showing a specific ad"""
def ad(request, pk):
    ad = Advertisement.objects.get(pk=pk)
    context = {'ad': ad}
    return render(request, 'sellyoshit/product_details.html', context)

