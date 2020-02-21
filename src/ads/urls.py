from django.urls import path
from . import views

urlpatterns = [
    #path('', views.test_view, name='test_view'),
    path('ads/', views.add_detail_view, name='fetch_add'),
    path('ads2/', views.create_add, name='create_add'),
    path('thanks/', views.response, name='thanks')

]