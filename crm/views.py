from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Voici la page d'accueil du site")