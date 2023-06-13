from django.urls import path
from bourse.views import index, description, ajouter_commentaire,actualites,detail_actualite

urlpatterns = [
    path('', index, name='home'),
    path('<int:entreprise_id>/', description, name='description'),
    path('ajouter_commentaire/<int:entreprise_id>/', ajouter_commentaire, name='ajouter_commentaire'),
    path('actualites/',actualites, name='actualites'),
    path('actualites/<int:article_id>/',detail_actualite, name='detail_actualite'),
]
