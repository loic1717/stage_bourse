from django.contrib import admin
from bourse.models import Entreprise,Article,Associer,Commentaire


 #Afficher dans la base de donnée en fesant une list_display et mettre se que l'on veut afficher qui se rouve dans le models
#affichage Entreprise
class AdminEntrprise(admin.ModelAdmin):
    list_display = (
        'nom', 'symbole_boursier', 'description', 'date_ajout'
    )
      #affichage Article
class AdminArticle(admin.ModelAdmin):
    list_display = (
        'titre', 'contenu', 'date_publication', 'public'
    )
    #affichage de l'association(Entreprise et article)
class AdminAssocier(admin.ModelAdmin):
    list_display = (
        'entreprise','article'
    )

class AdminCommmentaire(admin.ModelAdmin):
    list_display = ('entreprise', 'utilisateur', 'contenu', 'date_creation')


admin.site.register(Entreprise,AdminEntrprise)
admin.site.register(Article,AdminArticle)
admin.site.register(Associer,AdminAssocier)
admin.site.register(Commentaire,AdminCommmentaire)