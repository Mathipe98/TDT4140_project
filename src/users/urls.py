from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.show_user_profile, name='user_profile')
]
