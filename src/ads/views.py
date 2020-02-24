from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Advertisement
from .forms import AdvertisementForm
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Advertisement


def ad_detail_view(request):
    ad = Advertisement.objects.last()  # Henter kun siste element som ble lagt til
    context = {'ad': ad}
    return render(request, 'ads/fetch_ad.html', context)


def create_ad(request):
    user = request.user
    if not user.is_authenticated:
        redirect('ads_view')
    if request.method == "POST":
        form = AdvertisementForm(request.POST, initial={"header_picture": "default.png"})
        if form.is_valid():
            ad = form.save(commit=False)
            #ad.seller = user.userID
            ad.publish()
            ad.save()
            return redirect('thanks_response')
    form = AdvertisementForm
    return render(request, "ads/create_ad.html", {'form': form})


def thanks_response(request):
    # Should rather be dependent on user than primary key
    return render(request, "ads/thanks.html")


def advertisements_view(request):
    my_ads = Advertisement.objects.filter()
    # my_ad.publish()
    return render(request, 'ads/advertisement_view.html', {'ads': my_ads})


def show_specific_ad(request, pk):
    user = request.user
    # pk is passed from urls to this view. Must be identically named
    ad = get_object_or_404(Advertisement, pk=pk)
    # get_object_or_404 either gives object with pk or a 404 not found

    # if user.is_superuser or user.id == ad.seller.id:  # Should be replaced by better authentication
    #    return render(request, 'ads/advertisement_owner.html', {'ad': ad})
    # else:
    return render(request, 'ads/advertisement_owner.html', {'ad': ad})


def edit_ad(request, pk):
    ad = get_object_or_404(Advertisement, pk=pk)
    # Authentication needed
    if request.method == "POST":
        form = AdvertisementForm(request.POST, instance=ad)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.published_date = timezone.now()
            ad.save()
            return redirect('post_detail', pk=ad.pk)
    else:
        form = AdvertisementForm(instance=ad)
    return render(request, 'ads/edit_ad.html', {'form': form})
