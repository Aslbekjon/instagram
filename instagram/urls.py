from django.urls import path
from .views import index, profile, follow

urlpatterns = [
    path('index', index, name = 'index'),
    path('<slug:username>', profile, name="profile"),
    path('<username>/follow/<option>', follow, name='follow')
]
