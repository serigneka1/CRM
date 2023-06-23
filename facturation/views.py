from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Facture
from .forms import FactureForm

@login_required
def factures(request):
    factures = Facture.objects.all()
    context = {'factures': factures}
    return render(request, 'factures.html', context)

@login_required
def facturer(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            facture = form.save()
            return redirect('factures')
    else:
        form = FactureForm()
    context = {'form': form}
    return render(request, 'facturer.html', context)
