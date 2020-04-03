"""
Display different web pages all relating to the usage of advertisements

Functions:

    sell_ad(request, pk) : redirect
        Marks an ad as sold and records the time, after validating the user. Returns a redirect to the homepage.
    create_ad(request) : redirect (POST) / render (GET)
        Displays a page for creating a new ad. Redirects the user to it after creating it.
    show_specific_ad(request, pk) : render
        Returns a render of a page displaying the currently requested ad.
    edit_ad(request, pk) : redirect (POST) / render (GET)
         Lets the user change information on an already created ad.
    delete_ad(request, pk) : redirect
        View for deleting a requested ad. Returns redirect to homepage.

"""

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


def sell_ad(request, pk):
    """
    Marks an ad as sold and records the time, after validating the user. Returns a redirect to the homepage.

    :param request: A django HttpRequest object. The session of the user.
    :param pk: Primary key of the requested ad. Passed into the view via the url.
    :return:
        redirect: A redirect with the homepage as destination
    """
    user = request.user
    ad = get_object_or_404(Advertisement, pk=pk)  # Either gives the request ad, or a 404 page if the ad is not found
    if user.is_authenticated:  # Checks whether the user is logged in
        if user == ad.seller or user.admin:  # Checks if the user is the owner of the ad or an admin user
            ad.sold_date = timezone.now()
            ad.sold = True
            ad.save()  # Saves the updates to the advertisement model
    return redirect("home")  # Redirects the user to the homepage using the 'home' view


def create_ad(request):
    """
    Displays a page for creating a new ad. Redirects the user to it after creating it.

    :param request: A django HttpRequest object. The session of the user.
    :return:
        redirect (POST): A path to the created ad.
        render (GET): A render of the creation-page with a form for input
    """
    user = request.user
    if not user.is_authenticated:  # Checks whether the user is logged in
        return redirect('home')  # If not, redirect to the homepage
    if request.method == "POST":  # If the user is accessing the page via POST
        form = AdvertisementForm(request.POST, request.FILES)  
        if form.is_valid():
            ad = form.save(commit=False)  # Returns an object that has not been saved to db yet (commit=false)
            ad.seller = user
            ad.publish()  # Calls on the advertisement model's publish method, recording time of creation
            ad.save()  # Saves the model to the database
            return redirect('specific_ad', ad.pk)  # Redirects the user to the newly created ad
    form = AdvertisementForm  # Creates a new form for the advertisement model
    return render(request, "ads/create_ad.html", {'form': form, 'categories': Category.objects.all()})
    # Renders the create_ad HTML page with the newly created form, as well as sending in all the available categories
    # (all categories that currently exist in the database)


def show_specific_ad(request, pk):
    """
    Returns a render of a page displaying the currently requested ad.

    :param request: A django HttpRequest object. The session of the user.
    :param pk: Primary key of the requested ad. Passed into the view via the url.
    :return:
        render: A render with the advertisement.html file and the requested ad object
    """
    ad = get_object_or_404(Advertisement, pk=pk)
    # Either returns the requested object or a 404 not found
    return render(request, 'ads/advertisement.html', {'ad': ad, 'categories': Category.objects.all()})
    # Renders advertisement.html with the requested ad, as well as all available categories


def edit_ad(request, pk):
    """
    View for letting the user change information on an already created ad.

    :param request: A django HttpRequest object. The session of the user.
    :param pk: Primary key of the requested ad. Passed into the view via the url.
    :return:
        redirect (POST) : Redirect to the edited ad's page.
        render (GET) :  Render of the creation page with the information of the requested ad filled in.
    """
    ad = get_object_or_404(Advertisement, pk=pk)  # Either gives the request ad, or a 404 page if the ad is not found
    user = request.user
    if not user.is_authenticated:  # Checks whether the user is logged in
        if not user == ad.seller:  # Checks whether the user is the owner of the ad
            return redirect('specific_ad', ad.pk)  # Redirects to the ad's default page
    if request.method == "POST":  # If the view is being called with POST
        form = AdvertisementForm(request.POST, request.FILES, instance=ad)
        # Creates a form with ad's info already filled in
        if form.is_valid():  # Checks the validity of the input of the form's fields
            ad = form.save(commit=False)  # Returns an object that has not been saved to db yet (commit=false)
            ad.author = request.user
            ad.published_date = timezone.now()
            ad.save()  # Saves the ad to the database
            return redirect('specific_ad', pk=ad.pk)  # Redirects to the ad's default page
    else:
        form = AdvertisementForm(instance=ad)  # Creates a form with the requested ad's current information filled in
    return render(request, 'ads/create_ad.html', {'form': form, 'categories': Category.objects.all()})
    # Renders create_ad with the form already containing the requested ad's current info,
    # as well as all available categories


def delete_ad(request, pk):
    """
    View for deleting a requested ad. Returns redirect to homepage.

    :param request: A django HttpRequest object. The session of the user.
    :param pk: Primary key for the requested advertisement
    :return:
        redirect: A redirect to the homepage
    """
    ad = get_object_or_404(Advertisement, pk=pk)  # Either gives the request ad, or a 404 page if the ad is not found
    user = request.user
    if user.is_authenticated:  # Checks whether the user is logged in
        if user == ad.seller or user.admin:  # Checks whether the user is the owner of the ad or an admin
            ad.delete()  # Deletes the ad from the database
    return redirect('home')  # Redirects the user to the homepage of the site
