from django.urls import path
from . import views

app_name = 'leads'
urlpatterns=[

    path("", views.leads_list, name="leads_list"),
    path("add_lead/", views.add_lead, name="add_lead"),
    path("<int:pk>/", views.leads_detail, name="leads_detail"),

]