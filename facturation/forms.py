from django import forms
from .models import Facture, Article

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['numero', 'date', 'client', 'total']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['nom', 'prix']
