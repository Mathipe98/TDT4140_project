from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/dash/', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('<int:pk>/data/', views.pivot_data, name='pivot_data'),
]