from django.contrib import admin
from .models import Eleve, AbscenceEleve, Professeur, AbscenceProfesseur, Classe, Matiere, Controle, Note, EmploiDuTemps, Composition

# Inline pour les absences des élèves
class AbscenceEleveInline(admin.TabularInline):
    model = AbscenceEleve
    extra = 0

# Inline pour les absences des professeurs
class AbscenceProfesseurInline(admin.TabularInline):
    model = AbscenceProfesseur
    extra = 0

@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):
    inlines = [AbscenceEleveInline]
    list_display = ('id', 'nom', 'prenom', 'cin_eleve', 'classe', 'user_username', 'user_email', 'user_password')
    readonly_fields = ('user_username', 'user_email', 'user_password')
    list_filter = ('classe',)
    search_fields = ('nom', 'prenom', 'cin_eleve')

@admin.register(Professeur)
class ProfesseurAdmin(admin.ModelAdmin):
    inlines = [AbscenceProfesseurInline]
    list_display = ('nom', 'prenom', 'date_naissance', 'sexe', 'lieu_naissance', 'tel', 'classe')
    search_fields = ('nom', 'prenom')

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'annee_scolaire')
    search_fields = ('nom', 'annee_scolaire__annee')  # Utilisez la relation pour rechercher l'année scolaire

@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('nom', 'classe')
    search_fields = ('nom', 'classe__nom')  # Utilisez la relation pour rechercher la classe

@admin.register(Controle)
class ControleAdmin(admin.ModelAdmin):
    list_display = ('matiere', 'date', 'type', 'description')
    search_fields = ('matiere__nom', 'type')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('eleve', 'controle', 'note')
    search_fields = ('eleve__nom', 'controle__matiere__nom')

@admin.register(EmploiDuTemps)
class EmploiDuTempsAdmin(admin.ModelAdmin):
    list_display = ('classe', 'date_debut', 'date_fin', 'img')
    search_fields = ('classe__nom',)

@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
    list_display = ('classe', 'date_debut', 'date_fin', 'img')
    search_fields = ('classe__nom',)
