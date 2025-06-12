from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class areoportsForm(ModelForm):
    class Meta:
        model = models.Areoports
        fields = ('nom', 'pays')
        labels = {
        'nom' : _('Nom'),
        'pays' : _("Pays de localisation"),
        }

class pistesForm(ModelForm):
    class Meta:
        model = models.Pistes
        fields = ('num', 'areoports', 'longueur')
        labels = {
        'num' : _('Numéro de la piste'),
        'aréoports' : _("Aréoport d'appartennance") ,
        'longueur' : _('Longueur de la piste'),
        }

class compagniesForm(ModelForm):
    class Meta:
        model = models.Compagnies
        fields = ('nom', 'description', 'pays_ratt')
        labels = {
        'nom': _('Nom de la compagnie'),
        'description': _("Description"),
        'pays_ratt': _('Pays de rattachement'),
        }

class typesForm(ModelForm):
    class Meta:
        model = models.Types
        fields = ('marque', 'modele', 'description', 'longueur')
        labels = {
        'marque' : _('Nom de Région'),
        'modele' : _('Date de Création') ,
        'description' : _('Nombre de Départements'),
        #'images' : _('URL de la photo'),
        'longueur': _(' longueur de piste nécessaire'),
        }

class avionsForm(ModelForm):
    class Meta:
        model = models.Avions
        fields = ('nom', 'compagnie', 'modele')
        labels = {
        'nom' : _("Nom de l'avion"),
        'compagnie' : _('Nom de la compagnie') ,
        'modele' : _("Modele de l'avion"),
        }


class volsForm(ModelForm):
    class Meta:
        model = models.Vols
        fields = ('avions', 'pilote', 'areoports_dep', 'h_dep', 'areoports_arr', 'h_arr')
        labels = {
        'avions' : _('Avion'),
        'pilote' : _('Pilote du vol') ,
        'areoports_dep' : _('aéroport de départ'),
        'h_dep' : _('date et heure de départ'),
        'areoports_arr' : _("aéroport d'arrivée"),
        'h_arr' : _("date et heure d'arrivée")
        }