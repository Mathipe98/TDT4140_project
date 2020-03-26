from django.core.paginator import Paginator
from django.shortcuts import render

from ads.models import Advertisement, Category
"""
Django views that make up an intuitive browsable site with multiple pages 

Functions:

    products(request) : render
        View for showing all ads that are not sold, ordering them by date created 
        and paginating them over multiple pages
    ad(request, pk) : render
        View for showing a specific ad

"""

def products(request):
    """
    View for showing all ads that are not sold, ordering them by date created
    and paginating them over multiple pages

    :param request: A django HttpRequest object. The session of the user.
    :return:
        render: A render with the product_listEXT.html file
    """
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
    """
    View for showing a specific ad

    :param request: A django HttpRequest object. The session of the user.
    :param pk: Primary key of the requested ad. Passed into the view via the url.
    :return:
        render: A render with the product_details.html file and the requested ad object
    """
    ad = Advertisement.objects.get(pk=pk)
    context = {'ad': ad}
    return render(request, 'sellyoshit/product_details.html', context)