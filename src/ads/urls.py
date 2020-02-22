from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisements_view, name='ads_view'),
    path('<int:pk>/', views.show_specific_ad, name='specific_ad'),
    # <int:pk> means that django expects an int (pk) and will transfer
    # it to the view as such. Transfers pk = int to show_specific_ad
    path('ads/', views.ad_detail_view, name='fetch_ad'),
    path('new/', views.create_ad, name='create_ad'),
    path('thanks/', views.thanks_response, name='thanks_response'),
    path('edit/<int:pk>/', views.edit_ad, name='edit_ad')
]

