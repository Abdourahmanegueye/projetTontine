# Generated by Django 4.0 on 2024-04-30 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leapplica', '0004_alter_utilisateurs_options_grouptontine_auteur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grouptontine',
            name='auteur',
        ),
    ]