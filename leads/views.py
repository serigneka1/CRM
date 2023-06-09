from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from . forms import AddLeadForm
from .models import Lead
from team.models import Team
from client.models import Client


@login_required
def leads_list(request):
    leads= Lead.objects.filter(created_by=request.user, converted_to_client=False)
    return render(request, 'leads_list.html', {'leads':leads})


@login_required
def leads_detail(request, pk):
    lead=get_object_or_404(Lead, created_by=request.user, pk=pk)

    return render(request, 'leads_detail.html',{ 'lead':lead})



@login_required
def leads_delete(request, pk):
    lead=get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()
    messages.success(request, 'vous avez supprimé le prospect')
    return redirect('leads:leads_list')

@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, 'Les changement ont été effectués')
            return redirect('leads:leads_list')
    else:
        form=AddLeadForm(instance=lead)
        return render(request, 'leads_edit.html', {'form': form})


@login_required
def add_lead(request):
    if request.method=='POST':
        team = Team.objects.filter(created_by=request.user).first()
        form=AddLeadForm(request.POST)
        if form.is_valid():
            lead=form.save(commit=False)
            lead.created_by=request.user
            lead.team = team
            lead.save()
            messages.success(request, 'Un prospect a été ajouté')
            return redirect('leads:leads_list')
    else:
        form= AddLeadForm()
    return render(request, 'add_lead.html', {'form':form})


@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    team = Team.objects.filter(created_by=request.user).first()
    if team:
        client = Client.objects.create(
            name=lead.name,
            email=lead.email,
            description=lead.description,
            created_by=request.user,
            team=team,
        )
        lead.converted_to_client = True
        lead.save()
        messages.success(request, 'Le prospect est converti en un client')
    else:
        messages.error(request, 'Vous devez avoir une équipe pour convertir un prospect en client')

    return redirect('leads:leads_list')
