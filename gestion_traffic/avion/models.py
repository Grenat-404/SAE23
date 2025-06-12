from django.db import models

# Create your models here.
class Areoports(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    pays = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.nom

class Pistes(models.Model):
    num = models.IntegerField(blank=False)
    areoports = models.CharField(max_length=100, blank=False)
    longueur = models.IntegerField(blank = False)
    def __str__(self):
        return self.num

class Compagnies(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=True)
    pays_ratt = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.nom

class Types(models.Model):
    marque = models.CharField(max_length=100, blank=False)
    modele = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    images = models.ImageField(upload_to='avions/', blank=True, null=True)
    longueur = models.IntegerField(blank = False)
    def __str__(self):
        return self.marque

class Avions(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    compagnie = models.CharField(max_length=100, blank=True)
    modele = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.nom

class Vols(models.Model):
    avions = models.CharField(max_length=100, blank=False)
    pilote = models.CharField(max_length=100, blank=False)
    areoports_dep = models.CharField(max_length=100, blank=False)
    h_dep = models.DateTimeField()
    areoports_arr = models.CharField(max_length=100, blank=False)
    h_arr = models.DateTimeField()
    def __str__(self):
        return self.avion