from django.contrib import admin
from .models import Entreprise
from .models import Utilisateur
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UtilisateurAdmin(UserAdmin):
    list_display = ('user_id',"created_at")
    list_filter = ("role","is_active")
    readonly_fields =(
        "user_id",
        "created_at"
    )
    


class EntrepriseAdmin(admin.ModelAdmin):
    search_fields=('matricule_fiscale','type_entreprise')
    
admin.site.register(Entreprise,EntrepriseAdmin)
admin.site.register(Utilisateur, UtilisateurAdmin)

