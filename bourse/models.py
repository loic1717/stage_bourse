from tkinter import CASCADE
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _ 
from user.models import  UtilisateurModel
# Create your models here.
class Entreprise(models.Model):
    id_entreprise = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    symbole_boursier = models.CharField(max_length=50)
    description = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='bourse/image', null=True, blank=True)
#Pour retourner le nom dans la base de donnée au lieu Objet
    def __str__(self):
        return self.nom

class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=250)
    contenu = models.TextField()
    date_publication = models.DateField()
    public = models.BooleanField()
    def __str__(self):
            return self.titre
class Associer(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class Commentaire(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(UtilisateurModel, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.utilisateur.username} sur {self.entreprise.nom}"