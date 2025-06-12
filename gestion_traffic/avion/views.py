from django.shortcuts import render, get_object_or_404, redirect
from .forms import aeroportsForm, avionsForm, compagniesForm, pistesForm, typesForm, volsForm
from . import models
from django.urls import reverse

def index(request):
    apts = models.Aeroports.objects.all()
    return render(request, "index.html", {"Aeroports": apts})

# –– UTILS ––
def _handle_crud(request, Model, FormClass, template_list, template_add,
                 template_update, template_delete, context_name, redirect_name, pk_name='id'):
    """
    Générique pour LIST / ADD / EDIT / DELETE selon request.path
    Mais ici on l'appelle manuellement dans chaque view pour plus de clarté.
    """
    pass  # on n'utilise pas dans cette version, on garde views séparées

# –– Aéroports ––
def afficheAeroports(request):
    qs = models.Aeroports.objects.all()
    return render(request, "avion/afficheAeroports.html", {"object_list": qs})

def ajoutAeroports(request):
    if request.method == "POST":
        form = aeroportsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('avion:afficheAeroports')
    else:
        form = aeroportsForm()
    return render(request, "avion/ajoutAeroports.html", {"form": form})

def updateAeroports(request, id):
    inst = get_object_or_404(models.Aeroports, pk=id)
    if request.method == "POST":
        form = aeroportsForm(request.POST, request.FILES, instance=inst)
        if form.is_valid():
            form.save()
            return redirect('avion:afficheAeroports')
    else:
        form = aeroportsForm(instance=inst)
    return render(request, "avion/updateAeroports.html", {"form": form, "id": id})

def deleteAeroports(request, id):
    inst = get_object_or_404(models.Aeroports, pk=id)
    if request.method == "POST":
        inst.delete()
        return redirect('avion:afficheAeroports')
    return render(request, "avion/deleteAeroports.html", {"object": inst})

# –– Avions ––
def afficheAvions(request):
    qs = models.Avions.objects.all()
    return render(request, "avion/afficheAvions.html", {"object_list": qs})

def ajoutAvions(request):
    if request.method == "POST":
        form = avionsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('avion:afficheAvions')
    else:
        form = avionsForm()
    return render(request, "avion/ajoutAvions.html", {"form": form})

def updateAvions(request, id):
    inst = get_object_or_404(models.Avions, pk=id)
    if request.method == "POST":
        form = avionsForm(request.POST, request.FILES, instance=inst)
        if form.is_valid():
            form.save()
            return redirect('avion:afficheAvions')
    else:
        form = avionsForm(instance=inst)
    return render(request, "avion/updateAvions.html", {"form": form, "id": id})

def deleteAvions(request, id):
    inst = get_object_or_404(models.Avions, pk=id)
    if request.method == "POST":
        inst.delete()
        return redirect('avion:afficheAvions')
    return render(request, "avion/deleteAvions.html", {"object": inst})

# –– Compagnies ––
def afficheCompagnies(request):
    qs = models.Compagnies.objects.all()
    return render(request, "avion/afficheCompagnies.html", {"object_list": qs})

def ajoutCompagnies(request):
    if request.method == "POST":
        form = compagniesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('avion:afficheCompagnies')
    else:
        form = compagniesForm()
    return render(request, "avion/ajoutCompagnies.html", {"form": form})

def updateCompagnies(request, id):
    inst = get_object_or_404(models.Compagnies, pk=id)
    if request.method == "POST":
        form = compagniesForm(request.POST, request.FILES, instance=inst)
        if form.is_valid():
            form.save()
            return redirect('avion:afficheCompagnies')
    else:
        form = compagniesForm(instance=inst)
    return render(request, "avion/updateCompagnies.html", {"form": form, "id": id})

def deleteCompagnies(request, id):
    inst = get_object_or_404(models.Compagnies, pk=id)
    if request.method == "POST":
        inst.delete()
        return redirect('avion:afficheCompagnies')
    return render(request, "avion/deleteCompagnies.html", {"object": inst})

# –– Pistes ––
def affichePistes(request):
    qs = models.Pistes.objects.all()
    return render(request, "avion/affichePistes.html", {"object_list": qs})

def ajoutPistes(request):
    if request.method == "POST":
        form = pistesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('avion:affichePistes')
    else:
        form = pistesForm()
    return render(request, "avion/ajoutPistes.html", {"form": form})

def updatePistes(request, id):
    inst = get_object_or_404(models.Pistes, pk=id)
    if request.method == "POST":
        form = pistesForm(request.POST, request.FILES, instance=inst)
        if form.is_valid():
            form.save()
            return redirect('avion:affichePistes')
    else:
        form = pistesForm(instance=inst)
    return render(request, "avion/updatePistes.html", {"form": form, "id": id})

def deletePistes(request, id):
    inst = get_object_or_404(models.Pistes, pk=id)
    if request.method == "POST":
        inst.delete()
        return redirect('avion:affichePistes')
    return render(request, "avion/deletePistes.html", {"object": inst})

# –– Types ––
def afficheTypes(request):
    qs = models.Types.objects.all()
    return render(request, "avion/afficheTypes.html", {"object_list": qs})

def ajoutTypes(request):
    if request.method == "POST":
        form = typesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('avion:afficheTypes')
    else:
        form = typesForm()
    return render(request, "avion/ajoutTypes.html", {"form": form})

def updateTypes(request, id):
    inst = get_object_or_404(models.Types, pk=id)
    if request.method == "POST":
        form = typesForm(request.POST, request.FILES, instance=inst)
        if form.is_valid():
            form.save()
            return redirect('avion:afficheTypes')
    else:
        form = typesForm(instance=inst)
    return render(request, "avion/updateTypes.html", {"form": form, "id": id})

def deleteTypes(request, id):
    inst = get_object_or_404(models.Types, pk=id)
    if request.method == "POST":
        inst.delete()
        return redirect('avion:afficheTypes')
    return render(request, "avion/deleteTypes.html", {"object": inst})

# –– Vols ––
def afficheVols(request):
    qs = models.Vols.objects.all()
    return render(request, "avion/afficheVols.html", {"object_list": qs})

def ajoutVols(request):
    if request.method == "POST":
        form = volsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('avion:afficheVols')
    else:
        form = volsForm()
    return render(request, "avion/ajoutVols.html", {"form": form})

def updateVols(request, id):
    inst = get_object_or_404(models.Vols, pk=id)
    if request.method == "POST":
        form = volsForm(request.POST, request.FILES, instance=inst)
        if form.is_valid():
            form.save()
            return redirect('avion:afficheVols')
    else:
        form = volsForm(instance=inst)
    return render(request, "avion/updateVols.html", {"form": form, "id": id})

def deleteVols(request, id):
    inst = get_object_or_404(models.Vols, pk=id)
    if request.method == "POST":
        inst.delete()
        return redirect('avion:afficheVols')
    return render(request, "avion/deleteVols.html", {"object": inst})
