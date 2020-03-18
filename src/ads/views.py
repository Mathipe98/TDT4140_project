from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Advertisement
from .forms import AdvertisementForm
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Advertisement, Category


def create_ad(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('ads_view')
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)  # initial={"header_picture": "default.png"})
        if form.is_valid():
            ad = form.save(commit=False)
            ad.seller = user
            ad.publish()
            ad.save()
            return redirect('specific_ad', ad.pk)
    form = AdvertisementForm
    return render(request, "ads/create_ad.html", {'form': form})


def advertisements_view(request):
    my_ads = Advertisement.objects.all()
    return render(request, 'ads/advertisement_view.html', {'ads': my_ads})


def show_specific_ad(request, pk):
    user = request.user
    # pk is passed from urls to this view. Must be identically named
    ad = get_object_or_404(Advertisement, pk=pk)
    # get_object_or_404 either gives object with pk or a 404 not found
    if user.is_authenticated:
        if user == ad.seller or user.admin:
            return render(request, 'ads/advertisement_owner.html', {'ad': ad, 'categories': Category.objects.all()})
    return render(request, 'ads/advertisement.html', {'ad': ad})


def edit_ad(request, pk):
    ad = get_object_or_404(Advertisement, pk=pk)
    user = request.user
    if not user.is_authenticated:
        if not user == ad.seller:
            return redirect('specific_ad', ad.pk)
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.published_date = timezone.now()
            ad.save()
            return redirect('specific_ad', pk=ad.pk)
    else:
        form = AdvertisementForm(instance=ad)
    return render(request, 'ads/create_ad.html', {'form': form})


def delete_ad(request, pk):
    ad = get_object_or_404(Advertisement, pk=pk)
    user = request.user
    if user.is_authenticated:
        if user == ad.seller or user.admin:
            ad.delete()
    return redirect('ads_view')
