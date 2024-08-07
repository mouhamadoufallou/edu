from django.contrib import admin
from .models import *
"""
# Register your models here.

class EleveAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'classe', 'user_username', 'user_email', 'user_password')
    readonly_fields = ('user_username', 'user_email', 'user_password')

admin.site.register(Eleve, EleveAdmin)



from django.contrib import admin
from .models import Eleve, AbsenceEleve
"""
class AbsenceEleveInline(admin.TabularInline):
    model = AbscenceEleve
    extra = 0

@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):
    inlines = [AbsenceEleveInline]
    # Ajoutez d'autres champs à afficher dans la liste des élèves
    list_display = ('id','nom', 'prenom', 'cin_eleve', 'classe','user_username', 'user_email', 'user_password')
    # Ajoutez d'autres champs à utiliser pour le filtre
    list_filter = ('classe',)
    # Ajoutez d'autres champs à utiliser pour la recherche
    search_fields = ('nom', 'prenom', 'cin_eleve')
    
@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(EmploiDuTemps)
class EmploiDuTempsAdmin(admin.ModelAdmin):
    list_display = ('classe', 'date_debut', 'date_fin')
    
@admin.register(AnneScolaire)
class AnneScolaireAdmin(admin.ModelAdmin):
    list_display = ('annee', 'date_debut', 'date_fin', 'actif')
    list_filter = ('actif',)
    search_fields = ('annee',)