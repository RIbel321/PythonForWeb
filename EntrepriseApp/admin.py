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


admin.site.register(Entreprise)
admin.site.register(Utilisateur, UtilisateurAdmin)