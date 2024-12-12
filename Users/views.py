from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, aauthenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Или другая страница после успешной регистрации
        else:
            form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# Вход
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'autho.html', {'form': form})

# Выход
def user_logout(request):
    logout(request)
    return redirect('/login/')
