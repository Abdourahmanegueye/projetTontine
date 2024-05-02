from django import forms


class Loginform(forms.Form):
    nom = forms.CharField(label="Nom utilisateur", widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    pwd = forms.CharField(label="password utilisateur", widget=forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
    ))