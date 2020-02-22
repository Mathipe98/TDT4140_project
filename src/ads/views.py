from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Advertisement
from .forms import AdvertismentForm
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Advertisement


def ad_detail_view(request):
    ad = Advertisement.objects.last() # Henter kun siste element som ble lagt til
    context = {'ad': ad}
    return render(request, 'ads/fetch_ad.html', context)


def create_ad(request):
    if request.method == "POST":
        form = AdvertismentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ads/thanks/')
    form = AdvertismentForm
    return render(request, "ads/create_ad.html", {'form': form})


def response(request):
    return render(request, "ads/thanks.html", {})


def advertisements_view(request):
    my_ads = Advertisement.objects.filter()
    # my_ad.publish()
    return render(request, 'ads/advertisement_view.html', {'ads': my_ads})


def show_specific_ad(request, pk):
    user = request.user
    # pk is passed from urls to this view. Must be identically named
    ad = get_object_or_404(Advertisement, pk=pk)
    # get_object_or_404 either gives object with pk or a 404 not found

    if user.is_superuser or user.id == ad.seller.id:  # Should be replaced by better authentication
        return render(request, 'ads/advertisement_owner.html')
    else:
        return render(request, 'ads/advertisement_standard.html', {'ad': ad})


