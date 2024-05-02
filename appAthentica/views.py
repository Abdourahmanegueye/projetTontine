from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import Loginform

def login_viw(request):
    form = Loginform(request.POST or None)
    if form.is_valid():
        nom = form.cleaned_data.get("nom")
        pwd = form.cleaned_data.get("pwd")
        user = authenticate(username=nom, password=pwd)
        if user is not None:
            login(request,user)
            return redirect("/groups/")
    return render(request, "utilisateur/login.html", {"form":form})
