from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import searchView

app_name = 'search'
urlpatterns = [
    url('results/', searchView, name='searchResults'),

]
