from django.urls import path
from .views import login

app_name='shop'
urlpatterns = [
    path('login/', login, name='login'),
]