from django.urls import path
from . import views as av

urlpatterns = [
    path('', av.advertisements_view, name='ads_view'),
    path('<int:pk>/', av.show_specific_ad, name='specific_ad'),
    path('new/', av.create_ad, name='create_ad'),
    path('<int:pk>/edit/', av.edit_ad, name='edit_ad'),
    path('<int:pk>/delete/', av.delete_ad, name='delete_ad'),
    path('<int:pk>/update/', av.sold_ad, name='sold_ad')
]

