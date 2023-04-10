from django.contrib.auth.forms import UserCreationFrom
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationFrom):
    email=forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Adresse e-mail'}))
    first_name=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Prénom'}))
    last_name=CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nom de famille'}))

    class Meta:
        model = User
        fields = ("username", 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __int__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = "Nom d\'utilisateur"
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small> Maximum 150 caractères.Doit inclure des lettres, des chiffres, @/./+/-.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Mot de passe'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Ton mot de passe doit être différents  des autres informations personnelles.</li><li>Il doit contenir au moins 8 characters.</li></li><li>Le mot de passe ne peut pass être entièrement numérique.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmer le mot de passe'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Entrer le même mot de passe pour vérification.</small></span>'
