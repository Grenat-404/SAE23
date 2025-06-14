# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

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
