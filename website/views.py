from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
from team.models import Team


def site(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authentifier l'utilisateur
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, " Tu es connectés.")
            return redirect('website:site')
        else:
            messages.success(request, "Erreur de connexion. Veuillez réessayer.")
            return redirect('website:site')
    return render(request, "site.html")

def records(request):
    records = Record.objects.all()
    if request.user.is_authenticated:
        return render(request, 'records.html', {"records":records})
    else:
        messages.success(request, "Vous devez d'abord vous connectez !")
        return redirect('site')

def factures(request):
    return render(request, "factures.html")


def logout_user(request):
    logout(request)
    messages.success(request, "Tu es déconnecté ...")
    return redirect("website:site")

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            # Message success before redirect
            messages.success(request, 'Votre compte a été bien créé. Bienvenue chez vous !')
            return redirect('website:site')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {"form": form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record= Record.objects.get(id=pk)
        return render(request, 'record.html', {"customer_record":customer_record})
    else:
        messages.success(request, "Vous devez d'abord vous connectez !")
        return redirect('website:site')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "La personne a été bien supprimée de la liste...")
        return redirect( 'website:records')
    else:
        messages.success(request, "Vous devez d'abord vous connectez !")
        return redirect('website:site')


def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request, "Ajout réussit...")
                return redirect('website:records')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "Vous devez d'abord vous connectez...")
        return redirect('website:site')


def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Vous avez effectué des modifications...")
            return redirect('records')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "Vous devez d'abord vous connectez...")
        return redirect('website:site')

@login_required
def my_account(request):
    team=Team.objects.filter(created_by=request.user).first()
    return render(request, 'myaccount.html', {'team':team})