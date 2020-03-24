"""The urls that are valid for /ads/ and the views they are associated with

    Variables
        urlpatterns: List
            List of the valid urls and their corresponding views
"""

from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.show_user_profile, name='user_profile')
    # <int:pk> means that any integer passed into the url will be passed into the view's pk parameter
]
