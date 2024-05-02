from django.urls import path
from .views import (home, about, group_list, detail_group, new_group, modiffierGroup, list, 
                    supprimerGroup, new_utilisateur)

urlpatterns = [
    path("", home, name="index"),
    path("about/", about, name="about"),
    path("groups/", group_list, name="group_list"),
    path("groups/<int:id>", detail_group, name="detail_group"),
    path("groups/new", new_group, name="new_group"),
    path("groups/modif/<int:id>", modiffierGroup, name="modiffierGroup"),
    path("groups/delete/<int:id>", supprimerGroup, name="supprimerGroup"),
    path("group/new", new_utilisateur, name="new_utilisateur"),
    path("group/", list, name="listes"),
]
