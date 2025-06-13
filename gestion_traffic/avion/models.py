from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import make_aware, is_naive
from datetime import timedelta

# Create your models here.
class Aeroports(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    pays = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.nom
    class Meta:
        managed = False
        db_table = 'aeroports'

class Pistes(models.Model):
    num = models.IntegerField(blank=False)
    aeroports = models.ForeignKey('Aeroports', on_delete=models.CASCADE)
    longueur = models.IntegerField(blank = False)
    def __str__(self):
        return self.num

    class Meta:
        managed = False
        db_table = 'pistes_atterrissage'


class Compagnies(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=True)
    pays_ratt = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.nom

    class Meta:
        managed = False
        db_table = 'compagnies'

class Types(models.Model):
    marque = models.CharField(max_length=100, blank=False)
    modele = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    images = models.ImageField(upload_to='avions/', blank=True, null=True)
    longueur = models.IntegerField(blank = False)
    def __str__(self):
        return self.marque

    class Meta:
        managed = False
        db_table = 'types_avions'

class Avions(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    compagnie = models.ForeignKey('Compagnies', on_delete=models.CASCADE)
    modele = models.ForeignKey('Types', on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

    class Meta:
        managed = False
        db_table = 'avions'

class Vols(models.Model):
    avions = models.ForeignKey('Avions', on_delete=models.CASCADE, default=None)
    pilote = models.CharField(max_length=100, blank=False)
    aeroports_dep = models.ForeignKey('Aeroports', on_delete=models.CASCADE, related_name='vols_depart')
    h_dep = models.DateTimeField()
    aeroports_arr = models.ForeignKey('Aeroports', on_delete=models.CASCADE, related_name='vols_arrivee')
    h_arr = models.DateTimeField()

    def __str__(self):
        return f"{self.avions.nom} - {self.h_dep.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        managed = False
        db_table = 'vols'

    def clean(self):
        super().clean()
        erreurs = {}

        # Vérifie durée minimale
        if self.h_arr < self.h_dep + timedelta(minutes=10):
            erreurs['h_arr'] = "Le vol doit durer au moins 10 minutes."

        if is_naive(self.h_dep):
            self.h_dep = make_aware(self.h_dep)
        if is_naive(self.h_arr):
            self.h_arr = make_aware(self.h_arr)

        # Vérifie chevauchement
        dep_min = self.h_dep - timedelta(minutes=10)
        dep_max = self.h_dep + timedelta(minutes=10)
        arr_min = self.h_arr - timedelta(minutes=10)
        arr_max = self.h_arr + timedelta(minutes=10)

        conflits_dep = Vols.objects.filter(
            aeroports_dep=self.aeroports_dep,
            h_dep__range=(dep_min, dep_max)
        ).exclude(pk=self.pk)
        if conflits_dep.exists():
            erreurs['h_dep'] = "Conflit : un vol décolle déjà de cet aéroport dans les 10 minutes."

        conflits_arr = Vols.objects.filter(
            aeroports_arr=self.aeroports_arr,
            h_arr__range=(arr_min, arr_max)
        ).exclude(pk=self.pk)
        if conflits_arr.exists():
            erreurs['h_arr'] = "Conflit : un vol atterrit déjà à cet aéroport dans les 10 minutes."

        # Vérifie les pistes disponibles
        piste_min = self.avions.modele.longueur

        if not Pistes.objects.filter(aeroports=self.aeroports_dep, longueur__gte=piste_min).exists():
            erreurs['aeroports_dep'] = "Pas de piste assez longue à l'aéroport de départ."

        if not Pistes.objects.filter(aeroports=self.aeroports_arr, longueur__gte=piste_min).exists():
            erreurs['aeroports_arr'] = "Pas de piste assez longue à l'aéroport d'arrivée."

        if erreurs:
            raise ValidationError(erreurs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
