"""
Display different web pages all relating to the usage of the search function

Functions:
    searchView(request) : render
        Filters the advertisement objects based on search input

"""

from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from ads.models import Advertisement, Category
from django.core.paginator import Paginator

def searchView(request):
    """
    This view is initiated by the search-button. When this button is pressed the input in the search field with name
    'q' is sent to this view. This input field is used to filter the advertisement objects.

    :param request: A django HttpRequest object. The session of the user.
    :return:
        render: Render of the filtered advertisements
    """
    
    query = request.GET.get('q')    # receiving the query from input field name='q'

    # search the database title and body
    results = Advertisement.objects.filter(Q(product_name__icontains=query) | Q(product_description__icontains=query) | Q(category__name__icontains=query))

    paginator = Paginator(results, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'products': page_obj.object_list,
               'page_obj': page_obj,
               'categories': Category.objects.all()
    }

    return render(request, 'sellyoshit/search.html', context)
