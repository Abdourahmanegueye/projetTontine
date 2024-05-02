from django.db import models
from django.contrib.auth.models import User

class GroupTontine(models.Model):
    nom = models.CharField(max_length=150)
    nbPersonnes = models.CharField(max_length=150)
    montant = models.CharField(max_length=150)
    date_enrigistre = models.DateField(auto_now_add=True)
    # user = models.ForeignKey(Utilisateurs,on_delete=models.CASCADE)
    # auteur = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nom}{self.nbPersonnes} {self.montant} {self.date_enrigistre} "

class Utilisateurs(models.Model):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    telephone = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    adresse = models.CharField(max_length=150)
    date_inscrit = models.DateField(auto_now_add=True)
    # auteur = models.ForeignKey(User,on_delete=models.CASCADE)
    class  Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'
    
    def __str__(self):
        return f"{self.nom}{self.prenom} {self.telephone} {self.email} {self.adresse} {self.date_inscrit} "

class Membre(models.Model):
    nom = models.CharField(max_length=150)
    idgroup = models.ForeignKey(GroupTontine,on_delete=models.CASCADE)
    idutilisateur = models.ForeignKey(Utilisateurs,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom}{self.idgroup} {self.idutilisateur}  "