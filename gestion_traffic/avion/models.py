from datetime import timedelta

from django.core.exceptions import ValidationError
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
    avions = models.ForeignKey('Avions', on_delete=models.CASCADE, default=None)
    pilote = models.CharField(max_length=100, blank=False)
    aeroports_dep = models.ForeignKey('Aeroports', on_delete=models.CASCADE, related_name='vols_depart')
    h_dep = models.DateTimeField()
    aeroports_arr = models.ForeignKey('Aeroports', on_delete=models.CASCADE, related_name='vols_arrivee')
    h_arr = models.DateTimeField()

    def __str__(self):
        return f"{self.avions.nom} - {self.h_dep.strftime('%Y-%m-%d %H:%M')}"

    def clean(self):
        from django.utils.timezone import make_aware, is_naive

        super().clean()

        # Vérifie que l'écart entre départ et arrivée du vol est >= 10 minutes
        if self.h_arr < self.h_dep + timedelta(minutes=10):
            raise ValidationError("Le vol doit durer au moins 10 minutes.")

        # Plage de temps pour comparaison (±10 minutes)
        dep_min = self.h_dep - timedelta(minutes=10)
        dep_max = self.h_dep + timedelta(minutes=10)

        arr_min = self.h_arr - timedelta(minutes=10)
        arr_max = self.h_arr + timedelta(minutes=10)

        # Vols déjà existants qui se chevauchent en départ
        conflits_dep = Vols.objects.filter(
            aeroports_dep=self.aeroports_dep,
            h_dep__range=(dep_min, dep_max)
        ).exclude(pk=self.pk)

        if conflits_dep.exists():
            raise ValidationError("Un autre vol part déjà de cet aéroport à moins de 10 minutes d'écart.")

        # Vols déjà existants qui se chevauchent en arrivée
        conflits_arr = Vols.objects.filter(
            aeroports_arr=self.aeroports_arr,
            h_arr__range=(arr_min, arr_max)
        ).exclude(pk=self.pk)

        if conflits_arr.exists():
            raise ValidationError("Un autre vol arrive déjà à cet aéroport à moins de 10 minutes d'écart.")

        def save(self, *args, **kwargs):
            self.full_clean()
            super().save(*args, **kwargs)
