"""
    The urls that are valid for /messages/ and the views they are associated with

    Variables
        urlpatterns: List
            List of the valid urls and their corresponding views
"""

from django.urls import path
from . import views as cv

urlpatterns = [
    path('contact/<int:pk>/', cv.create_conversation, name='contact_user'),
    # <int:pk> means that any integer passed into the url will be passed into the view's pk parameter
    path('messages/<int:pk>', cv.send_message, name='messages'),
    path('view/', cv.thread_view, name='view-threads'),
    path('view/<int:thread_id>', cv.thread_view, name='view-threads')
    # <int:thread_id> means that any integer passed into the url will be passed into the view's thread_id parameter
]
