from django import forms
from .models import UtilisateurModel

class UtilisateurCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmer le mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = UtilisateurModel
        fields = ['username', 'email', 'password1', 'password2', 'region', 'ville', 'description']
