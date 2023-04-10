from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Vérifier si l'utilisateur est en train de se connecter
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authentifier l'utilisateur
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, " Tu es connecté.")
            return redirect('home')
        else:
            messages.success(request, "Erreur de connexion. Veuillez réessayer.")
            return redirect('home')
    return render(request, "home.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "Tu es déconnecté ...")
    return redirect("home")
def register_user(request):
    return render(request, 'register.html', {})