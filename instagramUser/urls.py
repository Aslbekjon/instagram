from django.urls import path
from .views import instaUsers

urlpatterns = [
    path('user/', instaUsers, name = 'instaUsers')
]
