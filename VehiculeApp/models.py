from django.db import models
from EntrepriseApp.models import Entreprise
from django.core.validators import MinValueValidator


class Vehicule(models.Model):
    capacite_kg= models.PositiveIntegerField(validators=[MinValueValidator(1,"La capacite doit etre superieure a 0 Skg")])


    immatriculation = models.CharField(
        max_length=100,
        unique = True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    entreprise= models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE
    )