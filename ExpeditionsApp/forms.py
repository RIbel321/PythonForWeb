from django import forms 
from .models import Expedition


class ExpeditionForm(forms.ModelForm):
    reference = forms.CharField(required=False, help_text="Laisser vide pour génération automatique.")

    class Meta:
        model = Expedition
        fields = [
            'reference',
            'type_entreprise',
            'adresse',
            'statut',
            'poids_kg',
            'entreprise',
        ]
