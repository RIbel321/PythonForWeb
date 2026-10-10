from django.db import models
from EntrepriseApp.models import Entreprise
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class Vehicule(models.Model):
    capacite_kg= models.PositiveIntegerField(validators=[MinValueValidator(1,"La capacite doit etre superieure a 0 Skg")])


    immatriculation = models.CharField(
        max_length=100,
        unique = True
    )

    disponible=models.BooleanField(default=True)


    type_vehicule = models.CharField(
    max_length=30,
    choices=[
        ('camionnette', 'Camionnette / utilitaire léger'),
        ('camion_porteur', 'Camion porteur'),
        ('semi_remorque', 'Semi-remorque'),
        ('fourgon', 'Fourgon'),
    ],
    null=True,
    blank=True
)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if(self.entreprise_id and self.entreprise.type_entreprise !='transporteur'):
            raise ValidationError('l  entreprise doit etre de type transporteur')

    def save(self ,*args,**kwargs):
        self.full_clean()
        super().save(*args,**kwargs)

    


    entreprise= models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE
    )