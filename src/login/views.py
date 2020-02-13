from django.shortcuts import render

def login(request):
    return render(request, 'sellyoshit/log_in.html')