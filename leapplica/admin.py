from django.contrib import admin
from .models import GroupTontine
from .models import Utilisateurs
from .models import Membre

admin.site.register(GroupTontine)
admin.site.register(Utilisateurs)
admin.site.register(Membre)