from django.conf.urls import url
from django.urls import path
from .views import signup
from .views import home
from .views import logins
from .views import logouts

app_name='shop'
urlpatterns = [
    path('', home, name='home'),
    path('login/', logins, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logouts, name='logout'),
]