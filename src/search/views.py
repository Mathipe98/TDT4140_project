from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from ads.models import Advertisement
from django.core.paginator import Paginator


def searchView(request):
    query = request.GET.get('q')    # receiving the query from input field name='q'

    # search the database title and body
    results = Advertisement.objects.filter(Q(product_name__icontains=query) | Q(product_description__icontains=query))

    print(len(results))
    print("searching for: " + query)
    paginator = Paginator(results, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'products': page_obj.object_list,
               'page_obj': page_obj}

    return render(request, 'sellyoshit/search.html', context)
