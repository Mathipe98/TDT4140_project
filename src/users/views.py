"""
Display the user profile of a specific user

Functions:

    show_user_profile(request, pk): render
        Returns a render with the specific information of a requested user

"""

from django.db.models import Avg
from django.shortcuts import render, get_object_or_404

from contact.models import Ratings
from users.models import Users


def show_user_profile(request, pk):
    """
    Finds a specific user via primary key. Returns a render with the specific information of that user.
    :param request: A django HttpRequest object. The session of the user.
    :param pk: The primary key of the requested user
    :return: render
                a render of the user_profile.html page with the specific information for that user
    """
    user = get_object_or_404(Users.objects.filter(pk=pk))
    # Either gives the request user, or a 404 page if the user is not found

    rating_count = Ratings.objects.filter(rated=user).count()
    # Gets amount of ratings and average score for the user
    rating_avg = Ratings.objects.filter(rated=user).aggregate(Avg('score'))
    return render(request, 'user_profile.html', {'rating_count': rating_count,
                                                 'rating_avg': rating_avg,
                                                 'user': user,
                                                 "request": request})
