from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/stats/', views.statistics_page, name='statistics_page'),
    path('<int:pk>/data/', views.pivot_data, name='pivot_data'),
]
