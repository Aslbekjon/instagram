from django.shortcuts import redirect, render
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SignUpForm
    return render(request, 'signup.html', {'form':form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, "login.html", {'form':form})
