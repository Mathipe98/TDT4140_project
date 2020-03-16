from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from ads.models import Advertisement
from django.core.paginator import Paginator
from dal import autocomplete


def searchView(request):
    query = request.GET.get('q')    # receiving the query from input field name='q'

    # search the database title and body
    results = Advertisement.objects.filter(Q(product_name__icontains=query) | Q(product_description__icontains=query)
                                           | Q(category__slug__icontains=query))

    paginator = Paginator(results, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'products': page_obj.object_list,
               'page_obj': page_obj}

    return render(request, 'sellyoshit/search.html', context)

class TagAutocomplete(autocomplete.Select2QuerySetView):
    """
    View for autocomplete widget
    """

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Advertisement.objects.none()

        qs = Advertisement.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs