from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    #page professeur
    path('professeur/mes_eleves/', views.list_eleves_professeur, name='list_eleves_professeur'),
    path('mes-matieres/', views.show_professeur_matieres, name='show_professeur_matieres'),
    path('mes-informations/', views.show_professeur_info, name='show_professeur_info'),

    #page de l'eleve
    path('mes-notes/', views.mes_notes, name='mes_notes'),
    path('mes-informations/', views.mes_informations, name='mes_informations'),
    # URL pour les absences de l'élève connecté
    path('absences/', views.mes_abscences, name='mes_abscences'),    # URL pour l'emploi du temps de l'élève connecté
    path('emploi-du-temps/', views.emploi_du_temps_eleve, name='emploi_du_temps_eleve'),
    # URL pour les compositions de l'élève connecté
    path('compositions/', views.compositions_eleve, name='compositions_eleve'),
        
    #Annee scolaire
    path('add-anne-scolaire/', views.add_anne_scolaire, name='add_anne_scolaire'),
    path('annee-scolaire/', views.show_annee_scolaire, name='show_annee_scolaire'),
    path('edit-anne-scolaire/<int:pk>/', views.edit_anne_scolaire, name='edit_anne_scolaire'),
    path('delete-anne-scolaire/<int:id>/', views.delete_annee, name='delete_annee'),
    
    #Copositions
    path('classe/<int:classe_id>/composition/', views.show_composition, name='show_composition'),
    path('classe/<int:classe_id>/composition/ajouter/', views.add_composition, name='add_composition'),
    path('show_composition_by_classe/', views.show_composition_by_classe, name='show_composition_by_classe'),
    path('composition/<int:composition_id>/supprimer/', views.delete_composition, name='delete_composition'),
    path('composition/<int:composition_id>/modifier/', views.edit_composition, name='edit_composition'),
    
    #Empoi du temps  
    path('classe/<int:classe_id>/emplois-du-temps/', views.show_emplois_du_temps, name='show_emplois_du_temps'),
    path('classe/<int:classe_id>/emplois-du-temps/ajouter/', views.add_emploi_du_temps, name='add_emploi_du_temps'),
    path('show_emplois_du_temps_by_classe/', views.show_emplois_du_temps_by_classe, name='show_emplois_du_temps_by_classe'),
    path('emplois-du-tps/<int:emploi_id>/supprimer/', views.delete_emploi_du_temps, name='delete_emploi_du_temps'),
    path('emplois-du-tps/<int:emploi_id>/modifier/', views.edit_emploi_du_temps, name='edit_emploi_du_temps'),

    #Abscence professeur
    path('abscences_prof/classe/<int:classe_id>/', views.abscences_prof_par_classe, name='abscences_prof_par_classe'),
    path('detail_abscence_prof/<int:id>/', views.detail_abscence_prof, name='detail_abscence_prof'),
    path('abscence_prof/<int:id>/', views.edit_abscence_prof, name='edit_abscence_prof'),
    path('ajouter_abscence_prof/<int:id>/', views.ajouter_abscence_prof, name='ajouter_abscence_prof'),
    path('delete_abscence_prof/<int:id>/', views.delete_abscence_prof, name='delete_abscence_prof'),

    #Professeur
    path('show_professeur/', views.show_professeur, name='show_professeur'),
    path('professeur/add/<int:classe_id>/', views.add_professeur, name='add_professeur'),
    path('professeurs/<int:classe_id>/', views.show_professeur_by_classe, name='show_professeur_by_classe'),
    path('professeur/edit/<int:id>/', views.edit_professeur, name='edit_professeur'),
    path('professeur/delete/<int:id>/', views.delete_professeur, name='delete_professeur'),
    path('detail_professeur/<int:id>/', views.detail_professeur, name='detail_professeur'),
    path('show_list_professeur_by_classe/', views.show_list_professeur_by_classe, name='show_list_professeur_by_classe'),
    # Classe Views
    path('add_classe/', views.add_classe, name='add_classe'),
    path('classes/edit/<int:id>/', views.edit_classe, name='edit_classe'),
    path('classes/delete/<int:id>/', views.delete_classe, name='delete_classe'),
    path('show_classe/', views.show_classe, name='show_classe'),
    path('show_list_eleve_by_classe/', views.show_list_eleve_by_classe, name='show_list_eleve_by_classe'),
    
    # Élève Views
    path('show_eleves/', views.show_eleves, name='show_eleves'),
    path('eleves/classe/<int:classe_id>/', views.show_eleves_by_class, name='show_eleves_by_class'),
    path('add_eleve/<int:classe_id>/', views.add_eleve, name='add_eleve'),
    path('edit_eleve/<int:id>/', views.edit_eleve, name='edit_eleve'),
    path('destroy_eleve/<int:id>/', views.destroy_eleve, name='destroy_eleve'),
    path('detail_eleve/<int:id>/', views.detail_eleve, name='detail_eleve'),
    
    # Absence Views
    path('abscences/classe/<int:classe_id>/', views.abscences_par_classe, name='abscences_par_classe'),
    path('detail_abscence/<int:id>/', views.detail_abscence, name='detail_abscence'),
    path('abscence/<int:id>/', views.edit_abscence, name='edit_abscence'),
    path('ajouter_abscence/<int:id>/', views.ajouter_abscence, name='ajouter_abscence'),
    path('delete_abscence/<int:id>/', views.delete_abscence, name='delete_abscence'),

    # Matière Views
    path('add_matiere/<int:classe_id>/', views.add_matiere, name='add_matiere'),
    path('add_matiere_by_classe/', views.add_matiere_by_classe, name='add_matiere_by_classe'),
    path('matieres/classe/<int:classe_id>/', views.show_matiere_by_classe, name='show_matiere_by_classe'),
    path('matiere/<int:matiere_id>/edit/', views.edit_matiere, name='edit_matiere'),
    path('delete_matiere/<int:matiere_id>/', views.delete_matiere, name='delete_matiere'),
    
    # Contrôle Views
    path('add_controle/<int:classe_id>/', views.add_controle, name='add_controle'),
    path('show_controle_by_classe/<int:classe_id>/', views.show_controle_by_classe, name='show_controle_by_classe'),
    path('edit_controle/<int:id>/', views.edit_controle, name='edit_controle'),
    path('delete_controle/<int:id>/', views.delete_controle, name='delete_controle'),

    # Notes Views
    path('add_notes/<int:controle_id>/', views.add_notes_for_all_students, name='add_notes_for_all_students'),
    path('notes/edit/<int:note_id>/', views.edit_note_view, name='edit_note'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('students_notes/<int:controle_id>/', views.students_notes, name='students_notes'),
    path('show_notes/', views.show_notes, name='show_notes'),
    path('show_notes_by_classe/<int:classe_id>/', views.show_notes_by_classe, name='show_notes_by_classe'),

    # Absence par Classe View
    path('show_abscence_by_classe/', views.show_abscence_by_classe, name='show_abscence_by_classe'),
    path('show_abscence_prof_by_classe/', views.show_abscence_prof_by_classe, name='show_abscence_prof_by_classe'),    
]
