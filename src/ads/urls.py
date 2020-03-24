"""The urls that are valid for /ads/ and the views they are associated with

    Variables
        urlpatterns: List
            List of the valid urls and their corresponding views
"""

from django.urls import path
from . import views as av

urlpatterns = [
    path('<int:pk>/', av.show_specific_ad, name='specific_ad'),
    # <int:pk> means that any integer passed into the url will be passed into the view's pk parameter
    path('new/', av.create_ad, name='create_ad'),
    path('<int:pk>/edit/', av.edit_ad, name='edit_ad'),
    path('<int:pk>/delete/', av.delete_ad, name='delete_ad'),
    path('<int:pk>/update/', av.sell_ad, name='sold_ad')
]
