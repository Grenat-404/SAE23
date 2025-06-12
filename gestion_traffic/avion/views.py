from django.shortcuts import render
from .forms import avionsForm
from .forms import pistesForm
from .forms import volsForm
from . import models
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
     [...] = models.[...].objects.all()
    return render(request, "avion/index.html", {"[...]": [...]})


#Aréoports
def ajoutAreoports(request):
    form = areoportsForm() # création d'un formulaire vide
    return render(request,"avion/ajoutAreoports.html",{"form" : form})

def traitementAreoportsAjout(request):
    if request.method == "POST":
        arform = avionsForm(request.POST, request.FILES)
        if arform.is_valid():
            Areoports = arform.save()
            return render(request, "avion/afficheAreoports.html", {"Areoports": Areoports})
        else:
            return render(request, "avion/ajoutAreoports.html", {"form": arform})
    else:
        return HttpResponseRedirect(reverse('ajoutAreoports'))

def traitementAreoportsModif(request, id):
    arform = areoportsForm(request.POST, request.FILES)
    if arform.is_valid():
        Areoports = arform.save(commit=False)
        Areoports.id = id
        Areoports.save()
        return render(request, "avion/afficheAreoports.html", {"Areoports": Areoports})
    else:
        return render(request, "avion/updateAreoports.html", {"form": arform, "id": id})

def readAreoports(request, id):
    Areoports = models.Areoports.objects.get(pk=id)
    return render(request,"avion/afficheAreoports.html",{"Areoports": Areoports})


def updateAreoports(request, id):
    Areoports = models.Areoports.objects.get(pk=id)
    if request.method == "POST":
        form = areoportsForm(request.POST)
        if form.is_valid():
            Areoports = form.save(commit=False)
            Areoports.id = id
            Areoports.save()
            return HttpResponseRedirect('')
    else:
        form = areoportsForm(instance=Areoports)
    return render(request, "avion/updateAreoports.html", {"form": form, "id": id})

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
