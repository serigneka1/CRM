from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('website/', include('website.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('facturation/', include('facturation.urls')),
    path('team/', include('team.urls')),
    path('todo/', include('todo.urls')),
    path('leads/', include('leads.urls')),
    path('client/', include('client.urls')),

]
