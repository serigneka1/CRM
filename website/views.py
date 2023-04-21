from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):
    records=Record.objects.all()
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
    else:
        return render(request, "home.html", {"records": records})

def logout_user(request):
    logout(request)
    messages.success(request, "Tu es déconnecté ...")
    return redirect("home")

def register_user(request):
    if request.method == "POST":
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username=form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            login(request, user)
            messages.success(request, 'Votre compte a été bien créé. Bienvenue chez vous !')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {"form":form})
    return render(request, 'register.html', {"form": form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record= Record.objects.get(id=pk)
        return render(request, 'record.html', {"customer_record":customer_record})
    else:
        messages.success(request, "Vous devez d'abord vous connectez !")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "La personne a été bien supprimée de la liste...")
        return redirect( 'home')
    else:
        messages.success(request, "Vous devez d'abord vous connectez !")
        return redirect('home')


def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request, "Ajout réussit...")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "Vous devez d'abord vous connectez...")
        return redirect('home')


def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Vous avez effectué des modifications...")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "Vous devez d'abord vous connectez...")
        return redirect('home')