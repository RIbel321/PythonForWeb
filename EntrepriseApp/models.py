from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.

matricule_fiscale_Validator = RegexValidator(regex=r'^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEadbnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$',message="Format attendu : 7 chiffres , 1 lettre (cle de controle) , 1 lettre(A/B/D/N/P) , 1 lettre (M/P/C/N/E) , 3 chiffres")

def validate_email(value):
    if not value.lower().endswith('@gmail.com'):
        raise ValidationError("Email must be a Gmail adress")

class Utilisateur(AbstractUser):
    user_id=models.CharField(max_length=8,primary_key=True)
    email=models.EmailField(unique=True,validators=[validate_email])
    role=models.CharField(max_length=20,choices=[
        ('chargeur','Chargeur'),
        ('transporteur','Transporteur'),
        ('administrateur','Admin'),
    ],default='chargeur')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        if not self.user_id :
            year=str(timezone.localdate().year)[-2:]
            prefix=year+"user"

            users=Utilisateur.objects.filter(user_id__startswith=prefix)
            users=users.order_by('-user_id')
            latest_user=users.first()

            if latest_user:
                last_number=int(latest_user.user_id[-2:])
                next_number=last_number+1
            else:
                next_number=0
            if next_number >99:
                raise ValueError("Maximum number of users reached for this year")
            self.user_id=prefix+str(next_number).zfill(2)
        self.full_clean()
        super().save(*args,**kwargs)



class Entreprise(models.Model):
    matricule_fiscal=models.CharField(max_length=17,unique=True,validators=[matricule_fiscale_Validator])
    type_entreprise=models.CharField(choices=[
        ('chargeur','Chargeur'),
        ('transporteur','Transporteur'),
        ])
    adresse=models.TextField()
    utilisateur=models.OneToOneField(Utilisateur,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
