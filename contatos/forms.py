from django import forms

from .models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ["nome", "telefone", "email"]
        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "input", "placeholder": "Nome completo"}
            ),
            "telefone": forms.TextInput(
                attrs={"class": "input", "placeholder": "(11) 99999-9999"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "input", "placeholder": "email@exemplo.com"}
            ),
        }
