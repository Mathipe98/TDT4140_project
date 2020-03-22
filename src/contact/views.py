"""
    Displays different web pages all relating to messages/ratings between users

    Functions
        determine_users_from_thread_id : user, user, thread
            Helper method used to determine which user is which in a thread
        save_msg_form(form, current_thread, user_to, user_from) : None
            Helper method used to save a message form to Message model
        create_conversation(request, pk) : redirect
            Creates a conversation between a user and the requested other user if it does not already exist
        send_message(request, pk) : redirect (POST) / render (GET)
            Allows the user to send a message to another user. Redirects to conversation thread upon sending.
        thread_view(request, pk) : redirect (POST) / render (GET)
            Renders a requested thread the user has with another other user and the messages between them

"""

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
    """
    Helper method used to determine which user is which in a thread

    :param user: The user who is requesting the view
    :param thread_id: The requested thread
    :return:
        ( None x 3 )
            Only if the user is not part of the requested thread
        user_from : User
            The user who is requesting the view
        user_to : User
            The other user who is part of the thread
        thread : Thread
            The thread between the two users
    """

    thread = get_object_or_404(Thread, pk=thread_id)
    # Returns the requested thread object, or renders a 404 page if not found
    user_from = user
    if user == thread.user1:
        user_to = thread.user2
    elif user == thread.user2:
        user_to = thread.user1
    else:  # This only happens if the user is not part of the thread
        return None, None, None
    return user_from, user_to, thread


def save_msg_form(form, current_thread, user_to, user_from):
    """
    Helper method used to save a form if the information is valid

    :param form: The MessageForm to be saved
    :param current_thread: The thread between the two users
    :param user_to: The user receiving the message
    :param user_from: The user sending the message
    :return: None
    """
    if form.is_valid():  # Checks that the input in the form is valid
        messages = form.save(commit=False)  # TODO: Explain line
        messages.thread = current_thread
        messages.sentto = user_to
        messages.sentfrom = user_from
        messages.publish()  # Calls the publish method in the Message model
        messages.save()  # Saves the model to the database


def create_conversation(request, pk):
    """
    Creates a new conversation between the logged in user and a requested other user. Returns redirect to send_message

    :param request: A django HttpRequest object. The session of the user.
    :param pk: The primary key of the User model. The requested user to initiate a conversation with.
    :return:
        redirect
            A redirect, either to home (validation fails) or send_message (successful)
    """
    user_from = request.user  # The user requesting the page
    if not user_from.is_authenticated:  # If the user is not logged in
        return redirect('home')  # Redirects to home page
    user_to = get_object_or_404(Users, pk=pk)
    # Returns either the requested User object or renders a 404 page if not found
    if user_from == user_to:  # Stops you from sending messages to yourself
        return redirect("home")
    if user_from.pk < pk:  # TODO: Explain line
        user1 = user_from
        user2 = user_to
    else:
        user1 = user_to
        user2 = user_from
    Thread.objects.get_or_create(user1=user1, user2=user2)  # Creates the thread if it does not exist
    thread = Thread.objects.get(user1=user1, user2=user2)  # Returns the requested Thread object
    return redirect("messages", pk=thread.pk)
    #  Redirects to the send_message view with the thread's primary key as argument


def send_message(request, pk):
    # TODO: Docstring
    user = request.user  # The user requesting the page
    if not user.is_authenticated:  # If the user is not logged in
        return redirect('home')  # Redirects to home page
    user_from, user_to, thread = determine_users_from_thread_id(user, pk)
    if user_from is None:  # Method returned redirect
        return redirect('home')
    text = "Send a message to " + user_to.username
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            save_msg_form(form, thread, user_to, user_from)
            return redirect('view-threads', thread.threadid)
    else:
        form = MessageForm
    return render(request, "sellyoshit/contact.html", {'text': text, 'form': form})


def thread_view(request, thread_id=-1):
    """
    Renders a requested thread the user has with another other user and the messages between them

    :param request: A django HttpRequest object. The session of the user.
    :param thread_id: Primary key of the requested thread. -1 by default
    :return:
        redirect (POST/failed validation)
            A redirect, either to home (failed validation) or to the thread_view with an updated thread (successful)
        render (GET)
            A render of message_view.html with the requested message thread
    """
    user = request.user  # The user requesting the page
    if not user.is_authenticated:  # If the user is not logged in
        return redirect('home')  # Redirects to home page

    messages = Messages.objects.filter(Q(sentto=user) | Q(sentfrom=user))
    #  This is a filter which checks if sentto OR sentfrom is the user. Returns a queryset of only those messages
    messages = messages.order_by('sent')  # Orders the queryset by the sent field in the model

    if thread_id == -1:  # If no specific thread is requested
        try:
            current_thread = messages.latest('sent').thread  # Gets the first thread by newest messages
        except ObjectDoesNotExist:  # If the user has no messages at all
            return render(request, 'message_view_failure.html',
                          {'message': 'You have not created any conversations yet'})
            #  Renders the failure page with the message
    else:
        try:  # A specific thread has been requested
            current_thread = messages.filter(thread=thread_id).latest('thread_id').thread
            # Filter which gets latest message from requested thread
        except ObjectDoesNotExist:  # If that thread does not exist or there are no messages at all
            return render(request, 'message_view_failure.html',
                          {'message': "There is no thread with this ID currently existing. Create a convo first"})
            # Renders the failure page with the message

    threads = []  # List for storing all threads, used for sidebar in html
    current_messages = []  # List for storing messages for current thread
    for message in messages:  # Reverses order of the messages so that most recent is displayed furthest down
        parent_thread = message.thread
        #  Finds the thread that the message belongs to by using the foreign key in message
        if parent_thread not in threads:  # If thread has not been recorded yet
            threads.append(parent_thread)
        if parent_thread == current_thread:
            current_messages.append(message)  # The message is part of the thread we are looking for
    user_from, user_to, thread = determine_users_from_thread_id(user, current_thread.pk)
    if user_from is None:  # Method returned redirect
        return redirect('home')
    try:
        rating = Ratings.objects.get(rated=user_to, ratedby=user_from)
        # Gets previous rating if they've already been rated
    except ObjectDoesNotExist:
        rating = 0
    if request.method == "POST":  # If the page is requested via POST
        form = MessageForm(request.POST)  # Creates a MessageForm with the POST-data
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
        form = MessageForm  # Creates a new MessageForm to be filled out
    return render(request,
                  'message_view.html',
                  {'threads': threads,
                   'user': user,
                   'current_thread': current_thread,
                   'current_messages': current_messages,
                   'rating': rating,
                   'form': form})
    # Renders message_view.html with the specific data gathered through the method
