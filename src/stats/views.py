from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from ads.models import Advertisement
from users.models import Users
from datetime import timedelta
from statistics import mean


def statistics_page(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('home')
    elif not user.admin:
        return redirect('home')
    else:
        return render(request, 'stats/statistics_page.html', statistics_context())


def statistics_context():
    users, ads = Users.objects.all(), Advertisement.objects.all()
    sold_items_count = len([ad for ad in ads if ad.sold])
    average_sell_seconds = mean([(ad.sold_date - ad.published_date).total_seconds() for ad in ads if ad.sold_date])
    average_sell_time = str(timedelta(seconds=average_sell_seconds)).split('.')[0]
    context = {'users_count': users.count(),
               'advertisements_count': ads.count(),
               'sold_items_count': sold_items_count,
               'average_sell_time': average_sell_time}
    return context


def pivot_data(request):
    dataset = Advertisement.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
