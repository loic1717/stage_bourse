from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UtilisateurModel

class UtilisateurCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmer le mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = UtilisateurModel
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'region', 'ville', 'description']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Les mots de passe sont différents !!')
        return password2
