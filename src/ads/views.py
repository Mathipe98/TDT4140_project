from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Advertisement
from .forms import Advertisment_form


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



