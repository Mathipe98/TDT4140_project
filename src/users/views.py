from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm,LoginForm

# Create your views here.
def signup(request):
        context = {}
        if request.POST:
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get("username")
                raw_password = form.cleaned_data.get("password1")
                user = authenticate(username=username,password = raw_password)
                login(request,user)
                return redirect('home')
            else:
                context['registration_form'] = form
        else:
            form =SignupForm()
            context['registration_form'] = form
        return render(request,"sellyoshit/log_in.html",context)

def logins(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('home')
    else:
        form = LoginForm()

    context['login_form'] = form
    return render(request,'sellyoshit/log_in.html',context)

def logouts(request):
    logout(request)
    return redirect('home')
