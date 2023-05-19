from django.urls import path
from . import views


app_name = 'facturation'
urlpatterns=[
    path("", views.factures, name="factures"),
    path('facturer', views.facturer, name='facturer')
]