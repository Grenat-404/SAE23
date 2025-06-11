from django.db import models

# Create your models here.
class Aréoports(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    pays = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.nom

class Pistes(models.Model):
    num = models.IntegerField(blank=False)
    aréoports = models.CharField(max_length=100, blank=False)
    longueur = models.IntegerField(blank = False)
    def __str__(self):
        return self.nom

class Compagnies(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    description = models.CharField(blank=True)
    pays_ratt = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.nom

class Types(models.Model):
    marque = models.CharField(max_length=100, blank=False)
    modele = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='chateaux/', blank=True, null=True)
    longueur = models.IntegerField(blank = False)
    def __str__(self):
        return self.nom

class Avions(models.Model):

    def __str__(self):
        return self.nom

class Vols(models.Model):

    longueur = models.IntegerField(blank = False)
    def __str__(self):
        return self.nom