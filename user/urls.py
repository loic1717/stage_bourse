from django.urls import path
from .views import ajout_utilisateur,login_view,logout_view

app_name = 'user'

urlpatterns = [
    path('ajout/', ajout_utilisateur, name='ajout_utilisateur'),
      path('login/', login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    # Ajoutez d'autres URL pour vos vues utilisateur
]
