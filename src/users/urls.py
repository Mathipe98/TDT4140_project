from django.conf.urls import url
from django.urls import path
from .views import signup
from .views import home

app_name='shop'
urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
]