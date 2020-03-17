from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import searchView
from django.urls import path
from .views import TagAutocomplete
from search import views

app_name = 'search'
urlpatterns = [
    url('results/', searchView, name='searchResults'),
    path('tag-autocomplete/', views.TagAutocomplete.as_view(), name='tag-autocomplete'),

]
