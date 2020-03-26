"""The urls that are valid for /search/ and the views they are associated with

    Variables
        urlpatterns: List
            List of the valid urls and their corresponding views
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import searchView

app_name = 'search'
urlpatterns = [
    url('results/', searchView, name='searchResults'),

]
