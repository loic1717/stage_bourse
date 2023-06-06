from django.shortcuts import render,redirect
from .models import Entreprise,Commentaire
from django.contrib.auth.decorators import login_required


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

def description(request, entreprise_id):
    entreprise = Entreprise.objects.get(pk=entreprise_id)
    context = {
        'entreprise': entreprise,
    }
    return render(request, 'bourse/description.html', context)



@login_required
def ajouter_commentaire(request, entreprise_id):
    # Récupérer l'entreprise associée à l'ID
    entreprise = Entreprise.objects.get(pk=entreprise_id)

    if request.method == 'POST':
        # Récupérer le contenu du commentaire depuis le formulaire
        contenu = request.POST.get('contenu')

        # Créer un nouvel objet Commentaire associé à l'entreprise et à l'utilisateur connecté
        commentaire = Commentaire.objects.create(
            entreprise=entreprise,
            utilisateur=request.user,
            contenu=contenu
        )

        # Enregistrer le commentaire dans la base de données
        commentaire.save()

        # Rediriger l'utilisateur vers la page de description de l'entreprise
        return redirect('description', entreprise_id=entreprise_id)

    # Préparer le contexte pour le rendu du template
    context = {
        'entreprise': entreprise,
    }

    return render(request, 'bourse/description.html', context)
