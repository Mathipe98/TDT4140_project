from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisements_view, name='ads_view'),
    path('<int:pk>/', views.show_specific_ad, name='specific_ad'),
    # <int:pk> means that django expects an int (pk) and will transfer
    # it to the view as such. Transfers pk = int to show_specific_ad
    #path('', views.test_view, name='test_view'),
    path('ads/', views.add_detail_view, name='fetch_add'),
    path('ads2/', views.create_add, name='create_add'),
    path('thanks/', views.response, name='thanks')

]

