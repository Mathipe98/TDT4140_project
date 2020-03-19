from django.db.models import Avg
from django.shortcuts import render, get_object_or_404

from contact.models import Ratings
from users.models import Users


def show_user_profile(request, pk):
    user = get_object_or_404(Users.objects.filter(pk=pk))

    # Gets amount of ratings and average score for the user
    rating_count = Ratings.objects.filter(rated=user).count()
    rating_avg = Ratings.objects.filter(rated=user).aggregate(Avg('score'))
    return render(request, 'user_profile.html', {'rating_count':rating_count,
                                                 'rating_avg':rating_avg,
                                                 'user': user,
                                                 "request": request})
