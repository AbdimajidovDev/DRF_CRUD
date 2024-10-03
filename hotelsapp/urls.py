from django.urls import path
from .views import *
urlpatterns = [
    path('', HotelView.as_view(), name='home'),
    path('<int:pk>/', HotelDetailView.as_view(), name='detail')
]
