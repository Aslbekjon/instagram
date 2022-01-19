from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='user_login')
def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, "profile.html")