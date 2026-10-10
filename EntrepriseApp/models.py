from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


def validate_email(value):
    if not value :
        raise ValidationError("L adresse email est obligatoire")
    if not value.endswith('@gmail.com'):
        raise ValidationError("Domaine Invalide")

class Utilisateur(AbstractUser):
    user_id = models.CharField(max_length=8, primary_key=True, editable=False)
    email = models.EmailField(unique=True,validators=[validate_email])
    telephone = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(max_length=20, choices=[
        ('chargeur', 'Chargeur'),
        ('transporteur', 'Transporteur'),
        ('administrateur', 'Administrateur'),
    ], default='chargeur')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

matricule_fiscale_Validator = RegexValidator(regex=r'^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEadbnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$',message="Format attendu : 7 chiffres , 1 lettre (cle de controle) , 1 lettre(A/B/D/N/P) , 1 lettre (M/P/C/N/E) , 3 chiffres")
   

class Entreprise(models.Model):
    raison_sociale = models.CharField(
        max_length=200,
        null=False,
        blank=False
        
    )
    matricule_fiscale = models.CharField(
        max_length=17,
        null=False,
        blank=False,
        unique=True,
        validators=[matricule_fiscale_Validator]
    )
    adresse = models.TextField(validators=[MinLengthValidator(20,"L adresse doit contenir au moins 20 caracteres")])
    type_entreprise = models.CharField(
        max_length=100,
        choices=[
            ('chargeur', 'Chargeur'),
            ('transporteur', 'Transporteur')
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    gerant = models.OneToOneField(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name='Entreprise'
    )