from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from ads.models import Advertisement, Category
#from users.models import Thread
from .forms import SignupForm, LoginForm


# Create your views here.
def signup(request):
    context = {'categories': Category.objects.all()}
    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            context['signup_form'] = form
    else:
        form = SignupForm()
        context['signup_form'] = form
    return render(request, "sellyoshit/log_inEXT.html", context)


def log_in(request):
    context = {'categories': Category.objects.all()}

    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    context['login_form'] = form
    return render(request, 'sellyoshit/log_inEXT.html', context)


def log_out(request):
    logout(request)
    return redirect('home')

def my_page(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('home')
    products = Advertisement.objects.all().filter(seller=user.userid)
    paginator = Paginator(products, 6)  # Show X products per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'products': page_obj.object_list,
               'page_obj': page_obj,
               'categories': Category.objects.all()
    }

    return render(request,'sellyoshit/mypage.html',context)

