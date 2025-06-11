from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class avionsForm(ModelForm):
    class Meta:
        model = models.Region
        fields = ('nom', 'date_crea', 'nbr_dep', 'superficie', 'info', 'image')
        labels = {
        'nom' : _('Nom de Région'),
        'date_crea' : _('Date de Création') ,
        'nbr_dep' : _('Nombre de Départements'),
        'superficie' : _('Superficie'),
        'info': _('Informations Complémentaires'),
        'image': _('URL de la photo')
        }

class pistesForm(ModelForm):
    class Meta:
        model = models.Pistes
        fields = ('num', 'aréoports', 'longueur')
        labels = {
        'num' : _('Numéro de la piste'),
        'aréoports' : _("Aréoport d'appartennance") ,
        'longueur' : _('Longueur de la piste'),
        }

class volsForm(ModelForm):
    class Meta:
        model = models.Vols
        fields = ('', '', '', '', '', '')
        labels = {
        '' : _(''),
        '' : _('') ,
        '' : _(''),
        '' : _(''),
        '' : _(''),
        '' : _('')
        }