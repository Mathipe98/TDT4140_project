from django.conf.urls import url
from django.urls import path
from .views import signup
from .views import home
from .views import log_in
from .views import log_out

app_name='shop'
urlpatterns = [
    path('', home, name='home'),
    path('login/', log_in, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', log_out, name='logout'),
]