from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import GroupTontine
from .models import Utilisateurs
# from .models import Membre

# Create your views here.
def home(request):
    return render(request, "pages/index.htm")

def about(request):
    return render(request, "pages/about.htm")

@login_required(login_url="login")
def group_list(request):
    user = request.user
    print(user)
    groups = GroupTontine.objects.all() # pour sible tous le table
    #groups = GroupTontine.objects.filter(Utilisateurs=user) # pour sible tous le table
    return render(request, "groups/group_list.htm", {"groups":groups})


@login_required(login_url="login")
def detail_group(request, id):
    group = get_object_or_404(GroupTontine, id=id)  # pour recuper 
    # group = get_object_or_404(Utilisateurs, id=id)  # pour recuper 
    return render(request, "groups/detail_group.htm", {"group":group})

def new_group(request):
    # if request.(self, *args, **kwargs):
    #     return super().(*args, **kwargs)
    if request.method == "POST":
        nom = request.POST['nom']
        nbPersonnes = request.POST['nbPersonnes']
        montant = request.POST['montant']
        group = GroupTontine.objects.create(
            nom=nom,
            nbPersonnes=nbPersonnes,
            montant=montant,
        )
        group.save()
        return redirect("/groups/")
    return render(request, "groups/new_group.htm")

def modiffierGroup(request, id):
    group = get_object_or_404(GroupTontine, id=id)
    if request.method == "POST":
        nom = request.POST['nom']
        nbPersonnes = request.POST['nbPersonnes']
        montant = request.POST['montant']
        modiff = GroupTontine.objects.filter(pk=group.id)
        modiff.update(
            nom=nom,
            nbPersonnes=nbPersonnes,
            montant=montant,
        )
        return redirect("/groups/")
    return render(request, "groups/modiffierGroup.htm", {"group":group})

@login_required(login_url="login")
def supprimerGroup(request, id):
    group = get_object_or_404(GroupTontine, id=id)
    if request.method == "POST":
        group.delete()
    return redirect(request,"groups/supprimerGroup.html")


# =====================
def list(request):
    lists = Utilisateurs.objects.all()  # pour recuper 
    # list = get_object_or_404(Utilisateurs, id=id)
    return render(request, "groups/list.htm", {"lists":lists})

def new_utilisateur(request):
    
    if request.method == "POST":
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        telephone = request.POST['telephone']
        email = request.POST['email']
        adresse = request.POST['adresse']
        group = Utilisateurs.objects.create(
            nom=nom,
            prenom=prenom,
            telephone=telephone,
            email=email,
            adresse=adresse,
        )
        group.save()
        return redirect("/groups/")
    
    return render(request, "groups/new_utilisateur.html")