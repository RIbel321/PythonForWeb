from django.db import models
from EntrepriseApp.models import Entreprise
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils import timezone

# Create your models here.


class Expedition(models.Model):
    reference=models.CharField(max_length=20,unique=True)
    type_entreprise=models.CharField(max_length=20,choices=[
        ('chargeur','Chargeur'),
        ('transporteur','Transporteur')
    ],default='chargeur')

    adresse=models.CharField(default="Tunis",max_length=50,validators=[MinLengthValidator(2)])

    statut=models.CharField(max_length=20,choices=[
        ('publiee','Publiee'),
        ('attribuee','Attribuee'),
        ('en_cours','En_cours'),
        ('livree','Livree'),
        ('annulee','Annulee'),
    ],default='publiee')
    poids_kg=models.DecimalField(max_digits=20,decimal_places=2,null=False)

    entreprise=models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE
    )
    created_at=models.DateTimeField(default=timezone.now())
    updated_at=models.DateTimeField(default=timezone.now())

    def save(self,*args,**kwargs):
        if not self.reference:
            current_year=str(timezone.localdate().year)[-2:]
            prefix="EXP"+current_year

            expeditions=Expedition.objects.filter(reference__startswith=prefix)
            exped=expeditions.order_by('-reference')
            latest_expeds=exped.first()

            if latest_expeds:
                last_exped=int(latest_expeds.reference[-2:])
                next_number=last_exped+1
            else:
                next_number=0
            if next_number >99999:
                raise ValueError("Maximum number of users reached for this year")
            self.reference=prefix+str(next_number).zfill(5)
        self.full_clean()
        super().save(*args,**kwargs)

    def clean(self):
        super().clean()
        if(self.entreprise_id and self.entreprise.type_entreprise!="chargeur"):
            raise ValidationError("L entreprise de cette expedition n est pas un chargeur")
        



