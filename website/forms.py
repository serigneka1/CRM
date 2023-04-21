from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Adresse e-mail'}))
    first_name=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Prénom'}))
    last_name=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nom de famille'}))

    class Meta:
        model = User
        fields = ("username", 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __int__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = "Nom d\'utilisateur"
        self.fields['username'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Mot de passe'
        self.fields['password1'].label = ''


        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmer'
        self.fields['password2'].label = ''

# Create Add Record Form

class AddRecordForm(forms.ModelForm):
    first_name=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Prénom ',"class":'form-control'}), label="")
    last_name =forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Nom ',"class":'form-control'}), label="")
    email=forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={'placeholder':'E-mail ',"class":'form-control'}), label="")
    phone=forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={'placeholder':'Téléphone ',"class":'form-control'}), label="")
    adress=forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={'placeholder':'Adresse ',"class":'form-control'}), label="")
    state=forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={'placeholder':'Pays ',"class":'form-control'}), label="")
    zipcode=forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={'placeholder':'Code Postal ',"class":'form-control'}), label="")

    class Meta:
        model=Record
        exclude=('user',)
