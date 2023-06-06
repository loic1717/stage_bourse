from django.urls import path
from bourse.views import index, description, ajouter_commentaire

urlpatterns = [
    path('', index, name='home'),
    path('<int:entreprise_id>/', description, name='description'),
    path('ajouter_commentaire/<int:entreprise_id>/', ajouter_commentaire, name='ajouter_commentaire'),
]
