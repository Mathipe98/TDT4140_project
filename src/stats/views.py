from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core import serializers
from ads.models import Advertisement

def dashboard_with_pivot(request):
    return render(request, 'stats/dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Advertisement.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)





