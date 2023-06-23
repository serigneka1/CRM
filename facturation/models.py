from django.db import models
from client.models import Client  # Assurez-vous d'importer le modèle Client depuis l'application client

class Facture(models.Model):
    numero = models.CharField(max_length=20)
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.numero

class Article(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.nom
