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
    contenu = models.CharField(max_length=250)
    date_publication = models.DateField()
    public = models.BooleanField()
    def __str__(self):
            return self.titre
class Associer(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
   