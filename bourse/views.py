from django.shortcuts import render
from .models import Entreprise

def index(request):
    # Récupérer toutes les entreprises
    entreprises = Entreprise.objects.all()

    # Récupérer le paramètre 'item-name' de la requête GET
    item_name = request.GET.get('item-name')

    # Vérifier si le paramètre 'item-name' est présent et non vide
    if item_name != '' and item_name is not None:
        # Filtrer les entreprises en fonction du nom (utilisation de 'nom__icontains' pour une recherche insensible à la casse)
        entreprises = entreprises.filter(nom__icontains=item_name)

    # Préparer le contexte pour le rendu du template
    context = {
        'entreprises': entreprises
    }

    # Rendre le template 'bourse/index.html' avec le contexte

    return render(request, 'bourse/index.html', context)
    
def description(request, myid):
    entreprise = Entreprise.objects.get(id_entreprise=myid)
    context = {
        'entreprise': entreprise
    }

    return render(request, 'bourse/description.html', context)

