from django.shortcuts import render
from leads.models import Lead
from client.models import Client

def dashboard(request):
    leads = Lead.objects.filter(created_by=request.user).order_by('-created_at')[:5]
    clients = Client.objects.filter(created_by=request.user).order_by('-created_at')[:5]

    context = {
        'leads': leads,
        'clients': clients,
    }

    return render(request, 'dashboard.html', context)
