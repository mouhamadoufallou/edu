from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    # Classe Views
    path('add_classe/', views.add_classe, name='add_classe'),
    path('classes/edit/<int:id>/', views.edit_classe, name='edit_classe'),
    path('classes/delete/<int:id>/', views.delete_classe, name='delete_classe'),
    path('show_classe/', views.show_classe, name='show_classe'),
    path('show_list_by_classe/', views.show_list_by_classe, name='show_list_by_classe'),
    
    # Élève Views
    path('show_eleves/', views.show_eleves, name='show_eleves'),
    path('eleves/classe/<int:classe_id>/', views.show_eleves_by_class, name='show_eleves_by_class'),
    path('add_eleve/<int:classe_id>/', views.add_eleve, name='add_eleve'),
    path('edit_eleve/<int:id>/', views.edit_eleve, name='edit_eleve'),
    path('update_eleve/<int:id>/', views.update_eleve, name='update_eleve'),
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
]
