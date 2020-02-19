from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Advertisement
# Create your views here.


def advertisements_view(request):
    my_ads = Advertisement.objects.filter()
    # my_ad.publish()
    return render(request, 'ads/advertisement_view.html', {'ads': my_ads})


def show_specific_ad(request, pk):
    # pk is passed from urls to this view. Must be identically named
    ad = Advertisement.objects.get_object_or_404(Advertisement, pk=pk)
    # get_object_or_404 either gives object with pk or a 404 not found
    return render(request, 'ads/advertisement.html', {'ad': ad})
