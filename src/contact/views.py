from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from users.models import Users
from .forms import MessageForm
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Thread
from .models import Messages


def create_conversation(request, pk):
    userFrom = request.user
    if not userFrom.is_authenticated:
        return redirect("home")
    userTo = get_object_or_404(Users, pk=pk)
    if (userFrom.userid < pk):
        user1 = userFrom
        user2 = userTo
    else:
        user1 = userTo
        user2 = userFrom
    Thread.objects.get_or_create(user1=user1, user2=user2)
    thread = Thread.objects.get(user1=user1, user2=user2)
    return redirect("messages", pk=thread.pk)


def view_conversation(request, pk):
    thread = Thread.objects.get(pk=pk)
    user = request.user
    if not user.is_authenticated:
        return redirect("home")

    userFrom = user
    if (user == thread.user1):
        userTo = thread.user2
    elif (user == thread.user2):
        userTo = thread.user1
    else:
        return redirect("home")
    # if(userFrom.userid < pk):
    #    user1 = userFrom
    #    user2 = userTo
    # else:
    #    user1 = userTo
    #    user2 = userFrom
    test = "User 1: " + str(userFrom.userid) + " User 2: " + str(userTo.userid)
    # Thread.objects.get_or_create(user1=user1,user2=user2)
    # threadUser = Thread.objects.get(user1=user1,user2=user2)
    # test = "User 1: " + str(user1.userid) + " User 2: " + str(user2.userid) + " " + str(threadUser)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            messageS = form.save(commit=False)
            messageS.thread = thread
            messageS.sentto = userTo
            messageS.sentfrom = userFrom
            messageS.publish()
            messageS.save()
            return redirect("contact", userTo.userid)
    else:
        form = MessageForm
    return render(request, "sellyoshit/contact.html", {'test': test, 'form': form})
