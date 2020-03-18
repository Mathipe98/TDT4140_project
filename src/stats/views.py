from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from ads.models import Advertisement


def statistics_page(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('home')
    elif not user.admin:
        return redirect('home')
    else:
        return render(request, 'stats/statistics_page.html', {})


def pivot_data(request):
    dataset = Advertisement.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
