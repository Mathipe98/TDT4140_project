from django.urls import path
from . import views as cv
urlpatterns = [
    path('contact/<int:pk>', cv.create_conversation, name='contact_user'),
    path('messages/<int:pk>', cv.view_conversation, name='messages'),
    path('view/', cv.thread_view, name='view-threads'),
    path('view/<int:thread_id>', cv.thread_view, name='view-threads')
]
