from django.shortcuts import render, get_object_or_404

from users.models import Users


def show_user_profile(request, pk):
    user = get_object_or_404(Users.objects.filter(pk=pk))
    return render(request, 'user_profile.html', {'user': user, "request": request})
