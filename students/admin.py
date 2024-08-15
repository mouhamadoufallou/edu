from django.contrib import admin
from .models import Eleve, AbscenceEleve, Classe, Professeur, AbscenceProfesseur, Matiere, Controle, Note

# Enregistrement du modèle Classe
@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ('nom',)  # Affiche le champ 'nom' dans la liste
    search_fields = ('nom',)  # Permet de rechercher par nom de classe

# Enregistrement du modèle Professeur
class AbscenceProfesseurInline(admin.TabularInline):
    model = AbscenceProfesseur
    extra = 0

@admin.register(Professeur)
class ProfesseurAdmin(admin.ModelAdmin):
    inlines = [AbscenceProfesseurInline]
    list_display = ('nom', 'prenom', 'date_naissance', 'classe', 'user_username', 'user_email', 'user_password')
    list_filter = ('classe',)
    search_fields = ('nom', 'prenom')

# Enregistrement du modèle Eleve avec AbsenceEleve en ligne
class AbscenceEleveInline(admin.TabularInline):
    model = AbscenceEleve
    extra = 0

@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):
    inlines = [AbscenceEleveInline]
    list_display = ('id', 'nom', 'prenom', 'cin_eleve', 'classe', 'user_username', 'user_email', 'user_password')
    list_filter = ('classe',)
    search_fields = ('nom', 'prenom', 'cin_eleve')

# Enregistrement des autres modèles
@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('nom', 'classe')
    list_filter = ('classe',)
    search_fields = ('nom',)

@admin.register(Controle)
class ControleAdmin(admin.ModelAdmin):
    list_display = ('matiere', 'date', 'type')
    list_filter = ('matiere', 'type')
    search_fields = ('matiere__nom', 'type')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('eleve', 'controle', 'note')
    list_filter = ('eleve', 'controle')
    search_fields = ('eleve__nom', 'controle__matiere__nom')
