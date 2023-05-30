from django.shortcuts import render, redirect
from .forms import UtilisateurCreationForm
from .models import UtilisateurModel
def ajout_utilisateur(request):
    form = UtilisateurCreationForm()
    if request.method == 'POST':
        form = UtilisateurCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user/connection.html')  # Remplacez "nom_de_l_url_de_redirection" par le nom de l'URL de redirection après l'ajout réussi de l'utilisateur
    return render(request, 'user/ajout_utilisateur.html', {'form': form})
