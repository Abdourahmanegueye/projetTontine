# Generated by Django 4.0 on 2024-05-01 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leapplica', '0006_grouptontine_auteur_utilisateurs_auteuruser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grouptontine',
            name='auteur',
        ),
        migrations.RemoveField(
            model_name='utilisateurs',
            name='auteurUser',
        ),
    ]