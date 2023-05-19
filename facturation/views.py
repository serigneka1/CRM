from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def factures(request):
    return render(request, 'factures.html')


@login_required
def facturer(request):
    return render(request, 'facturer.html')