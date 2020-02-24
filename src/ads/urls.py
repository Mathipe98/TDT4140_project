from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisements_view, name='ads_view'),
    path('<int:pk>/', views.show_specific_ad, name='specific_ad'),
    path('new/', views.create_ad, name='create_ad'),
    path('<int:pk>/edit/', views.edit_ad, name='edit_ad'),
    path('<int:pk>/delete/', views.delete_ad, name='delete_ad')
]

