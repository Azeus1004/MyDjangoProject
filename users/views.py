from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = AuthenticationForm()
    return render(request, 'users/register.html', {'form': form})
# Create your views here.

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
    else:
        form = AuthenticationForm()
        
    return render(request, 'users/login.html', {'form':form})
def user_logout(request):
    logout(request)
    return redirect('/login')

@login_required
def dashboard(request):
    return render(request, "users/dashboard.html")