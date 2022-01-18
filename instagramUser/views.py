from django.shortcuts import render

# Create your views here.

def instaUsers(request):
    return render(request, 'instaUsers.html')