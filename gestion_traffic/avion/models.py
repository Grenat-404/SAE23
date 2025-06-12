from django.db import models

# Create your models here.
class Aeroports(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    pays = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.nom

class Pistes(models.Model):
    num = models.IntegerField(blank=False)
    aeroports = models.ForeignKey('Aeroports', on_delete=models.CASCADE)
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
    compagnie = models.ForeignKey('Compagnies', on_delete=models.CASCADE)
    modele = models.ForeignKey('Types', on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Vols(models.Model):
    avions = models.ForeignKey('Avions',on_delete=models.CASCADE, default=None)
    pilote = models.CharField(max_length=100, blank=False)
    aeroports_dep = models.ForeignKey('Aeroports', on_delete=models.CASCADE, related_name='vols_depart')
    h_dep = models.DateTimeField()
    aeroports_arr = models.ForeignKey('Aeroports', on_delete=models.CASCADE, related_name='vols_arrivee')
    h_arr = models.DateTimeField()
    def __str__(self):
        return self.avions