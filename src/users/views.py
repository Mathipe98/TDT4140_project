from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm

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

def home(request):
    return render(request, 'sellyoshit/home_page.html')
