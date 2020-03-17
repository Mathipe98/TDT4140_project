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
from django.db.models import Q


def determine_users_from_thread_id(user, thread_id):
    """ HELPER METHOD """
    thread = Thread.objects.get(pk=thread_id)
    user_from = user
    if user == thread.user1:
        user_to = thread.user2
    elif user == thread.user2:
        user_to = thread.user1
    else:
        return redirect("home")
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
    userFrom = request.user
    if not userFrom.is_authenticated:
        return redirect('home')
    userTo = get_object_or_404(Users, pk=pk)
    if userFrom == userTo:  # Stops you from sending messages to yourself
        return redirect("home")
    if userFrom.userid < pk:
        user1 = userFrom
        user2 = userTo
    else:
        user1 = userTo
        user2 = userFrom
    Thread.objects.get_or_create(user1=user1, user2=user2)
    thread = Thread.objects.get(user1=user1, user2=user2)
    return redirect("messages", pk=thread.pk)


def view_conversation(request, pk):
    user = request.user
    if not user.is_authenticated:
        return redirect('home')
    user_from, user_to, thread = determine_users_from_thread_id(user, pk)
    test = "User 1: " + str(user_from.userid) + " User 2: " + str(user_to.userid)
    # Thread.objects.get_or_create(user1=user1,user2=user2)
    # threadUser = Thread.objects.get(user1=user1,user2=user2)
    # test = "User 1: " + str(user1.userid) + " User 2: " + str(user2.userid) + " " + str(threadUser)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            save_msg_form(form, thread, user_to, user_from)
            return redirect('contact_user', user_to.userid)
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
    threads = []  # List for storing all threads, used for sidebar in html
    current_messages = []  # List for storing messages for current thread
    if thread_id == -1:  # If no specific thread is requested
        current_thread = messages.latest('sent').thread  # Gets the first thread by newest messages
    else:
        current_thread = messages.filter(thread=thread_id).latest('thread_id').thread
        # Gets latest message form requested thread

    for message in messages:
        parent_thread = message.thread
        #  Finds the thread that the message belongs to by using the foreign key in message
        if parent_thread not in threads:  # If thread has not been recorded yet
            threads.append(parent_thread)
        if parent_thread == current_thread:
            current_messages.append(message)  # The message is part of the thread we are looking for

    user_from, user_to, thread = determine_users_from_thread_id(user, current_thread.pk)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            save_msg_form(form, thread, user_to, user_from)
            return redirect('view-threads', thread.threadid)
    else:
        form = MessageForm
    return render(request,
                  'message_view.html',
                  {'threads': threads,
                   'user': user,
                   'current_thread': current_thread,
                   'current_messages': current_messages,
                   'form': form})
