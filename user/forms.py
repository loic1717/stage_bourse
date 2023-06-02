from django import forms
from .models import UtilisateurModel

#CLass pour les mots de passe et montrer à la base de donnée que l'on inssert des mots de passe

class UtilisateurCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmer le mot de passe', widget=forms.PasswordInput)
    
# Pour afficher dse que l'on veut dans le formuulaire
    class Meta:
        model = UtilisateurModel
        fields = ['username', 'first_name', 'last_name','email','password1', 'password2', 'region', 'ville', 'description']
