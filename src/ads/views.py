from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Advertisement
from .forms import Advertisment_form
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Advertisement

"""def create_add(request):
    adds = Advertisement.objects.all()
    context = {'adds': adds}
    return render(request, 'ads/fetch_add.html', context)"""

def add_detail_view(request):
    ad = Advertisement.objects.last() #Henter kun siste element som ble lagt til
    context = {'ad': ad}
    return render(request, 'ads/fetch_add.html', context)

def create_add(request):
    if request.method == "POST":
        form = Advertisment_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ads/thanks/')
    form = Advertisment_form
    return render(request, "ads/create_add.html", {'form': form})

def response(request):
    return render(request, "ads/thanks.html", {})


def advertisements_view(request):
    my_ads = Advertisement.objects.filter()
    # my_ad.publish()
    return render(request, 'ads/advertisement_view.html', {'ads': my_ads})


def show_specific_ad(request, pk):
    # pk is passed from urls to this view. Must be identically named
    ad = get_object_or_404(Advertisement, pk=pk)
    # get_object_or_404 either gives object with pk or a 404 not found
    return render(request, 'ads/advertisement.html', {'ad': ad})


