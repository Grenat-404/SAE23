from django.shortcuts import render
from .forms import avionsForm
from .forms import pistesForm
from .forms import volsForm
from . import models
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    Region = models.Region.objects.all()
    return render(request, "avion/index.html", {"Region": Region})

#Avions
def ajoutAvions(request):
    form = avionsForm() # création d'un formulaire vide
    return render(request,"avion/ajoutAvions.html",{"form" : form})

def traitementAvionsAjout(request):
    if request.method == "POST":
        aform = avionsForm(request.POST, request.FILES)
        if aform.is_valid():
            Avions = aform.save()
            return render(request, "avion/afficheAvions.html", {"Avions": Avions})
        else:
            return render(request, "avion/ajoutAvions.html", {"form": aform})
    else:
        return HttpResponseRedirect(reverse('ajoutAvions'))

def traitementAvionsModif(request, id):
    aform = avionsForm(request.POST, request.FILES)
    if aform.is_valid():
        Avions = aform.save(commit=False)
        Avions.id = id
        Avions.save()
        return render(request, "avion/afficheAvions.html", {"Avions": Avions})
    else:
        return render(request, "avion/updateAvions.html", {"form": aform, "id": id})

def readAvions(request, id):
    Avions = models.Avions.objects.get(pk=id)
    return render(request,"avion/afficheAvions.html",{"Avions": Avions})


def updateAvions(request, id):
    Avions = models.Avions.objects.get(pk=id)
    if request.method == "POST":
        form = avionsForm(request.POST)
        if form.is_valid():
            Avions = form.save(commit=False)
            Avions.id = id
            Avions.save()
            return HttpResponseRedirect('')
    else:
        form = avionsForm(instance=Avions)
    return render(request, "avion/updateAvions.html", {"form": form, "id": id})



def deleteAvions(request, id):
    Region = models.Region.objects.get(pk=id)
    if request.method == "POST":
        Region.delete()
        return HttpResponseRedirect(reverse('index'))
    return render(request, "chateauAPP/deleteRegion.html", {"Region": Region})


#CRUD Pistes
def ajoutChateau(request):
    form = chateauForm() # création d'un formulaire vide
    return render(request,"chateauAPP/ajoutChateau.html",{"form" : form})

def traitementChateau(request):
    cform = chateauForm(request.POST, request.FILES)
    if cform.is_valid():
        chateau = cform.save(commit=False)  # on crée une instance du modèle Château
        chateau.save()                      # on sauve l'instance, pas la classe
        return render(request, "chateauAPP/afficheChateau.html", {"Chateau": chateau})
    else:
        return render(request, "chateauAPP/ajoutChateau.html", {"form": cform})

def readChateau(request, id):
    Chateau = models.Chateau.objects.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"chateauAPP/afficheChateau.html",{"Chateau": Chateau})


def updateChateau(request, id):
    Chateau = models.Chateau.objects.get(pk=id)
    if request.method == "POST":
        form = chateauForm(request.POST, request.FILES)
        if form.is_valid():
            Chateau = form.save(commit=False)
            Chateau.id = id
            Chateau.save()
            return HttpResponseRedirect('')
    else:
        form = chateauForm(instance=Chateau)
    return render(request, "chateauAPP/updateChateau.html", {"form": form, "id": id})

def deleteChateau(request, id):
    Chateau = models.Chateau.objects.get(pk=id)
    if request.method == "POST":
        Chateau.delete()
        return HttpResponseRedirect(reverse('index'))
    return render(request, "chateauAPP/deleteChateau.html", {"Chateau": Chateau})


#CRUD Vols
def ajoutChateau(request):
    form = chateauForm() # création d'un formulaire vide
    return render(request,"chateauAPP/ajoutChateau.html",{"form" : form})

def traitementChateau(request):
    cform = chateauForm(request.POST, request.FILES)
    if cform.is_valid():
        chateau = cform.save(commit=False)  # on crée une instance du modèle Château
        chateau.save()                      # on sauve l'instance, pas la classe
        return render(request, "chateauAPP/afficheChateau.html", {"Chateau": chateau})
    else:
        return render(request, "chateauAPP/ajoutChateau.html", {"form": cform})

def readChateau(request, id):
    Chateau = models.Chateau.objects.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"chateauAPP/afficheChateau.html",{"Chateau": Chateau})


def updateChateau(request, id):
    Chateau = models.Chateau.objects.get(pk=id)
    if request.method == "POST":
        form = chateauForm(request.POST, request.FILES)
        if form.is_valid():
            Chateau = form.save(commit=False)
            Chateau.id = id
            Chateau.save()
            return HttpResponseRedirect('')
    else:
        form = chateauForm(instance=Chateau)
    return render(request, "chateauAPP/updateChateau.html", {"form": form, "id": id})

def deleteChateau(request, id):
    Chateau = models.Chateau.objects.get(pk=id)
    if request.method == "POST":
        Chateau.delete()
        return HttpResponseRedirect(reverse('index'))
    return render(request, "chateauAPP/deleteChateau.html", {"Chateau": Chateau})