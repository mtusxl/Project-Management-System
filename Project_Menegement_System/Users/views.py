from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, aauthenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
        else:
            form = RegistrationForm()
    return render(request, 'register.html', {'form': RegistrationForm})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            logout(request)
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'autho.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Вы успешно вышли из системы.")
    return redirect('login')

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get("name")
        last_name = request.POST.get("lastname")
        email = request.POST.get('email')

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return redirect("profile")
    return render(request, "profile.html")
