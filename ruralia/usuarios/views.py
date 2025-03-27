from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistroForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Si ya está logueado, lo enviamos a la app principal

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('app')  # Redirige a la app
    else:
        form = LoginForm()

    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige al login

def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('app')
        else:
            print(form.errors)  # Esto imprimirá los errores en la consola del servidor
    else:
        form = RegistroForm()
    
    return render(request, 'usuarios/register.html', {'form': form})
