from django import forms 
from . import models
from .models import Entreprise


class EntrepriseForm(forms.ModelForm):
    class Meta :
        model=Entreprise
        fields = [
            'matricule_fiscal',
            'type_entreprise',
            'adresse',
            'utilisateur',
        ]
        # widgets= {'created_at':forms.DateInput(attrs={'type':'date'})}