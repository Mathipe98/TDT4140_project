""" Django views functions used for displaying stats site data

    Functions:
        statistics_pages
        statistics_context
        pivot_data
"""

from datetime import timedelta
from statistics import mean

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect

from ads.models import Advertisement
from users.models import Users


def statistics_page(request):
    """ Checks if the user is authorized, and redirects to home page or renders the statistics page appropriately

        Parameters:
            request (class): A Django request object

        Returns:
            HttpResponse (class) or HttpResponseRedirect (class): Django HTTP response objects
    """
    user = request.user
    if not user.is_authenticated:
        return redirect('home')
    elif not user.admin:
        return redirect('home')
    else:
        return render(request, 'stats/statistics_page.html', statistics_context())


def statistics_context():
    """ Returns relevant statistics based on current site users and advertisements

        Returns:
            context (dict): Contains counts of site users, advertisements and
                            number of sold items, as well as average sell time of items
    """
    users, ads = Users.objects.all(), Advertisement.objects.all()
    sold_items_count = len([ad for ad in ads if ad.sold])
    sold_ads = [ad for ad in ads if ad.sold_date]
    if sold_ads:
        average_sell_seconds = mean([(ad.sold_date - ad.published_date).total_seconds() for ad in sold_ads])
        average_sell_time = str(timedelta(seconds=average_sell_seconds)).split('.')[0]
    else:
        average_sell_time = 'N/A'
    context = {'users_count': users.count(),
               'advertisements_count': ads.count(),
               'sold_items_count': sold_items_count,
               'average_sell_time': average_sell_time}
    return context


def pivot_data(request):
    """ Serializes and returns the data of all Advertisement objects as a JSON response

            Parameters:
                request (class): A Django request object

            Returns:
                JsonResponse (class): A Django JSON HTTP response object containing all Advertisement data
        """
    dataset = Advertisement.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
