from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.utils import timezone
from users.models import Users
from .forms import MessageForm
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Thread, Ratings
from .models import Messages
from django.db.models import Q, Model


def determine_users_from_thread_id(user, thread_id):
    """ HELPER METHOD """
    thread = get_object_or_404(Thread, pk=thread_id)
    user_from = user
    if user == thread.user1:
        user_to = thread.user2
    elif user == thread.user2:
        user_to = thread.user1
    else:
        return None, None, None
    return user_from, user_to, thread


def save_msg_form(form, current_thread, user_to, user_from):
    """ HELPER METHOD """
    if form.is_valid():
        messages = form.save(commit=False)
        messages.thread = current_thread
        messages.sentto = user_to
        messages.sentfrom = user_from
        messages.publish()
        messages.save()


def create_conversation(request, pk):
    user_from = request.user
    if not user_from.is_authenticated:
        return redirect('home')
    user_to = get_object_or_404(Users, pk=pk)
    if user_from == user_to:  # Stops you from sending messages to yourself
        return redirect("home")
    if user_from.pk < pk:
        user1 = user_from
        user2 = user_to
    else:
        user1 = user_to
        user2 = user_from
    Thread.objects.get_or_create(user1=user1, user2=user2)
    thread = Thread.objects.get(user1=user1, user2=user2)
    return redirect("messages", pk=thread.pk)


def view_conversation(request, pk):
    user = request.user
    if not user.is_authenticated:
        return redirect('home')
    user_from, user_to, thread = determine_users_from_thread_id(user, pk)
    if user_from is None:  # Method returned redirect
        return redirect('home')
    test = "User 1: " + str(user_from.userid) + " User 2: " + str(user_to.userid)
    # Thread.objects.get_or_create(user1=user1,user2=user2)
    # threadUser = Thread.objects.get(user1=user1,user2=user2)
    # test = "User 1: " + str(user1.userid) + " User 2: " + str(user2.userid) + " " + str(threadUser)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            save_msg_form(form, thread, user_to, user_from)
            return redirect('view-threads', thread.threadid)
    else:
        form = MessageForm
    return render(request, "sellyoshit/contact.html", {'test': test, 'form': form})


def thread_view(request, thread_id=-1):
    user = request.user
    if not user.is_authenticated:
        return redirect('home')

    messages = Messages.objects.filter(Q(sentto=user) | Q(sentfrom=user))
    #  This is a filter which checks if sentto OR sentfrom is the user
    messages = messages.order_by('sent')

    if thread_id == -1:  # If no specific thread is requested
        try:
            current_thread = messages.latest('sent').thread  # Gets the first thread by newest messages
        except ObjectDoesNotExist:
            return render(request, 'message_view_failure.html',
                          {'message': 'You have not created any conversations yet'})
    else:
        try:
            current_thread = messages.filter(thread=thread_id).latest('thread_id').thread
        # Gets latest message form requested thread
        except ObjectDoesNotExist:
            return render(request, 'message_view_failure.html',
                          {'message': "There is no thread with this ID currently existing. Create a convo first"})

    threads = []  # List for storing all threads, used for sidebar in html
    current_messages = []  # List for storing messages for current thread
    for message in messages.reverse():
        parent_thread = message.thread
        #  Finds the thread that the message belongs to by using the foreign key in message
        if parent_thread not in threads:  # If thread has not been recorded yet
            threads.append(parent_thread)
        if parent_thread == current_thread:
            current_messages.append(message)  # The message is part of the thread we are looking for
    current_messages.reverse()
    user_from, user_to, thread = determine_users_from_thread_id(user, current_thread.pk)
    try:
        rating = Ratings.objects.get(rated=user_to, ratedby=user_from)  # Gets previous rating if they've already been
        # rated
    except:
        rating = 0
    if user_from is None:  # Method returned redirect
        return redirect('home')
    if request.method == "POST":
        form = MessageForm(request.POST)
        if 'message' in request.POST:  # Function to execute if user sends message
            if form.is_valid():
                save_msg_form(form, thread, user_to, user_from)
                return redirect('view-threads', thread.threadid)
        elif 'rating' in request.POST:  # Function to execute if user rates the other user
            if rating == 0:  # If the logged in user has not rated the other user
                rating = Ratings.objects.create(rated=user_to, ratedby=user_from, score=request.POST.get('rating'))
                rating.save()
            else:  # Updates if the logged in user has already rated the other user
                new_rating = Ratings.objects.get(ratingid=rating.ratingid)
                new_rating.score = request.POST.get('rating')
                new_rating.save()
            return redirect('view-threads', thread.threadid)
    else:
        form = MessageForm
    return render(request,
                  'message_view.html',
                  {'threads': threads,
                   'user': user,
                   'current_thread': current_thread,
                   'current_messages': current_messages,
                   'rating': rating,
                   'form': form})
