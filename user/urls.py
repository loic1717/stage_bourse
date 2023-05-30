from django.urls import path
from .views import ajout_utilisateur

app_name = 'user'

urlpatterns = [
    path('ajout/', ajout_utilisateur, name='ajout_utilisateur'),
    # Ajoutez d'autres URL pour vos vues utilisateur
]
