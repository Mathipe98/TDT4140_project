"""pu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from sellyoshit import views
from login import views as lv
from ads import views as av
from search import views as sv
from contact import views as cv
from django.conf.urls.static import static
from django.conf import settings

# Used to import pictures
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.products, name='home'),
    path('admin/', admin.site.urls),
    path('shop/', include('sellyoshit.urls'), name='shop'),
    path('signup/', lv.signup, name='signup'),
    path('login/', lv.log_in, name='login'),
    path('logout/', lv.log_out, name='logout'),
    path('ademin/', lv.ademin, name='ademin'),
    path('mypage/', lv.my_page, name='mypage'),
    path('ads/', include('ads.urls'), name='Advertisements'),
    path('', av.advertisements_view, name='ads_view'),
    path('<int:pk>/', av.show_specific_ad, name='specific_ad'),
    path('new/', av.create_ad, name='create_ad'),
    path('<int:pk>/edit/', av.edit_ad, name='edit_ad'),
    path('<int:pk>/delete/', av.delete_ad, name='delete_ad'),
    path('results/', sv.searchView, name='search_results'),
    path('user/', include('users.urls'), name='user'),
    path('messages/', include('contact.urls'), name='contact'),
]

# For displaying imagefields
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
