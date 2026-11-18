from django import forms
from .models import Offres


class OffresForm(forms.ModelForm):
    class Meta:
        model = Offres
        fields = [
            'prix',
            'delai_jours',
            'statut',
            'expedition',
            'transporteur',
            'vehicule',
        ]

# Alias for convenience
OffreForm = OffresForm

