from django.shortcuts import render
from .forms import avionsForm, compagniesForm, typesForm, aeroportsForm
from .forms import pistesForm
from .forms import volsForm
from . import models
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
     Aeroports = models.Aeroports.objects.all()
     return render(request, "avion/index.html", {"Aeroports": Aeroports})


#Aréoports
def ajoutAeroports(request):
    form = aeroportsForm() # création d'un formulaire vide
    return render(request,"avion/ajoutAeroports.html",{"form" : form})

def traitementAeroportsAjout(request):
    if request.method == "POST":
        aeform = avionsForm(request.POST, request.FILES)
        if aeform.is_valid():
            Aeroports = aeform.save()
            return render(request, "avion/afficheAeroports.html", {"Areoports": Aeroports})
        else:
            return render(request, "avion/ajoutAeroports.html", {"form": aeform})
    else:
        return HttpResponseRedirect(reverse('ajoutAeroports'))

def traitementAreoportsModif(request, id):
    aeform = aeroportsForm(request.POST, request.FILES)
    if aeform.is_valid():
        Aeroports = aeform.save(commit=False)
        Aeroports.id = id
        Aeroports.save()
        return render(request, "avion/afficheAeroports.html", {"Aeroports": Aeroports})
    else:
        return render(request, "avion/updateAeroports.html", {"form": aeform, "id": id})

def readAeroports(request, id):
    Aeroports = models.Aeroports.objects.get(pk=id)
    return render(request,"avion/afficheAeroports.html",{"Aeroports": Aeroports})


def updateAeroports(request, id):
    Aeroports = models.Aeroports.objects.get(pk=id)
    if request.method == "POST":
        form = aeroportsForm(request.POST)
        if form.is_valid():
            Aeroports = form.save(commit=False)
            Aeroports.id = id
            Aeroports.save()
            return HttpResponseRedirect('')
    else:
        form = aeroportsForm(instance=Aeroports)
    return render(request, "avion/updateAeroports.html", {"form": form, "id": id})


#Pistes
def ajoutPistes(request):
    form = pistesForm() # création d'un formulaire vide
    return render(request,"avion/ajoutPistes.html",{"form" : form})

def traitementPistesAjout(request):
    if request.method == "POST":
        pform = pistesForm(request.POST, request.FILES)
        if pform.is_valid():
            Pistes = pform.save()
            return render(request, "avion/affichePistes.html", {"Pistes": Pistes})
        else:
            return render(request, "avion/ajoutPistes.html", {"form": pform})
    else:
        return HttpResponseRedirect(reverse('ajoutPistes'))

def traitementPistesModif(request, id):
    pform = pistesForm(request.POST, request.FILES)
    if pform.is_valid():
        Pistes = pform.save(commit=False)
        Pistes.id = id
        Pistes.save()
        return render(request, "avion/affichePistes.html", {"Pistes": Pistes})
    else:
        return render(request, "avion/updatePistes.html", {"form": pform, "id": id})

def readPistes(request, id):
    Pistes = models.Pistes.objects.get(pk=id)
    return render(request,"avion/affichePistes.html",{"Pistes": Pistes})


def updatePistes(request, id):
    Pistes = models.Pistes.objects.get(pk=id)
    if request.method == "POST":
        form = pistesForm(request.POST)
        if form.is_valid():
            Pistes = form.save(commit=False)
            Pistes.id = id
            Pistes.save()
            return HttpResponseRedirect('')
    else:
        form = pistesForm(instance=Pistes)
    return render(request, "avion/updatePistes.html", {"form": form, "id": id})


#Compagnies
def ajoutCompagnies(request):
    form = compagniesForm() # création d'un formulaire vide
    return render(request,"avion/ajoutCompagnies.html",{"form" : form})

def traitementCompagniesAjout(request):
    if request.method == "POST":
        cform = compagniesForm(request.POST, request.FILES)
        if cform.is_valid():
            Compagnies = cform.save()
            return render(request, "avion/afficheCompagnies.html", {"Compagnies": Compagnies})
        else:
            return render(request, "avion/ajoutCompagnies.html", {"form": cform})
    else:
        return HttpResponseRedirect(reverse('ajoutCompagnies'))

def traitementCompagniesModif(request, id):
    cform = compagniesForm(request.POST, request.FILES)
    if cform.is_valid():
        Compagnies = cform.save(commit=False)
        Compagnies.id = id
        Compagnies.save()
        return render(request, "avion/afficheCompagnies.html", {"Compagnies": Compagnies})
    else:
        return render(request, "avion/updateCompagnies.html", {"form": cform, "id": id})

def readCompagnies(request, id):
    Compagnies = models.Compagnies.objects.get(pk=id)
    return render(request,"avion/afficheCompagnies.html",{"Compagnies": Compagnies})


def updateCompagnies(request, id):
    Compagnies = models.Compagnies.objects.get(pk=id)
    if request.method == "POST":
        form = compagniesForm(request.POST)
        if form.is_valid():
            Compagnies = form.save(commit=False)
            Compagnies.id = id
            Compagnies.save()
            return HttpResponseRedirect('')
    else:
        form = pistesForm(instance=Compagnies)
    return render(request, "avion/updateCompagnies.html", {"form": form, "id": id})


#Types
def ajoutTypes(request):
    form = typesForm() # création d'un formulaire vide
    return render(request,"avion/ajoutTypes.html",{"form" : form})

def traitementTypesAjout(request):
    if request.method == "POST":
        tform = compagniesForm(request.POST, request.FILES)
        if tform.is_valid():
            Types = tform.save()
            return render(request, "avion/afficheTypes.html", {"Types": Types})
        else:
            return render(request, "avion/ajoutTypes.html", {"form": tform})
    else:
        return HttpResponseRedirect(reverse('ajoutTypes'))

def traitementTypesModif(request, id):
    tform = typesForm(request.POST, request.FILES)
    if tform.is_valid():
        Types = tform.save(commit=False)
        Types.id = id
        Types.save()
        return render(request, "avion/afficheTypes.html", {"Types": Types})
    else:
        return render(request, "avion/updateTypes.html", {"form": tform, "id": id})

def readTypes(request, id):
    Types = models.Compagnies.objects.get(pk=id)
    return render(request,"avion/afficheTypes.html",{"Types": Types})


def updateTypes(request, id):
    Types = models.Types.objects.get(pk=id)
    if request.method == "POST":
        form = typesForm(request.POST)
        if form.is_valid():
            Types = form.save(commit=False)
            Types.id = id
            Types.save()
            return HttpResponseRedirect('')
    else:
        form = typesForm(instance=Types)
    return render(request, "avion/updateTypes.html", {"form": form, "id": id})


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
    return render(request, "avion/deleteAvions.html", {"Region": Region})


#Vols
def ajoutVols(request):
    form = volsForm() # création d'un formulaire vide
    return render(request,"avion/ajoutVols.html",{"form" : form})

def traitementVolsAjout(request):
    if request.method == "POST":
        vform = volsForm(request.POST, request.FILES)
        if vform.is_valid():
            Vols = vform.save()
            return render(request, "avion/afficheVols.html", {"Vols": Vols})
        else:
            return render(request, "avion/ajoutVols.html", {"form": vform})
    else:
        return HttpResponseRedirect(reverse('ajoutVols'))

def traitementVolsModif(request, id):
    vform = volsForm(request.POST, request.FILES)
    if vform.is_valid():
        Vols = vform.save(commit=False)
        Vols.id = id
        Vols.save()
        return render(request, "avion/afficheVols.html", {"Vols": Vols})
    else:
        return render(request, "avion/updateVols.html", {"form": vform, "id": id})

def readVols(request, id):
    Vols = models.Vols.objects.get(pk=id)
    return render(request,"avion/afficheVols.html",{"Vols": Vols})


def updateVols(request, id):
    Vols = models.Vols.objects.get(pk=id)
    if request.method == "POST":
        form = volsForm(request.POST)
        if form.is_valid():
            Vols = form.save(commit=False)
            Vols.id = id
            Vols.save()
            return HttpResponseRedirect('')
    else:
        form = volsForm(instance=Vols)
    return render(request, "avion/updateVols.html", {"form": form, "id": id})



def deleteVols(request, id):
    Vols = models.Vols.objects.get(pk=id)
    if request.method == "POST":
        Vols.delete()
        return HttpResponseRedirect(reverse('index'))
    return render(request, "avion/deleteVols.html", {"Vols": Vols})