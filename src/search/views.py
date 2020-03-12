from django.shortcuts import render
from django.views.generic.list import ListView
from ads.models import Advertisement

class SearchView(ListView):
    model = Advertisement
    template_name = 'search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Advertisement.objects.filter(title__contains=query)
          result = postresult
       else:
           result = None
       return result
