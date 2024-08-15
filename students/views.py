from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required


@login_required
def add_anne_scolaire(request):
    if request.method == 'POST':
        form = AnneScolaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_annee_scolaire')
    else:
        form = AnneScolaireForm()
    return render(request, 'annee_scolaire/add_anne_scolaire.html', {'form': form})
@login_required
def show_annee_scolaire(request):
    annees = AnneScolaire.objects.all()
    return render(request, 'annee_scolaire/show_annee_scolaire.html', {'annees': annees})
@login_required
def edit_anne_scolaire(request, pk):
    anne_scolaire = get_object_or_404(AnneScolaire, pk=pk)
    if request.method == 'POST':
        form = AnneScolaireForm(request.POST, instance=anne_scolaire)
        if form.is_valid():
            form.save()
            return redirect('show_annee_scolaire')  
    else:
        form = AnneScolaireForm(instance=anne_scolaire)
    return render(request, 'annee_scolaire/edit_anne_scolaire.html', {'form': form})
@login_required
def delete_annee(request, id):
    annee = get_object_or_404(AnneScolaire, id=id)
    annee.delete()
    return redirect('show_annee_scolaire')
@login_required
def add_classe(request):
    if request.method == "POST": 
        form = ClasseForm(request.POST)
        if form.is_valid():
            classe = form.save(commit=False)
            annee_scolaire_id = request.POST.get('annee_scolaire')

            # Vérifiez si l'ID est fourni et s'il correspond à une année scolaire
            if annee_scolaire_id:
                try:
                    annee_scolaire = AnneScolaire.objects.get(id=annee_scolaire_id)
                    classe.annee_scolaire = annee_scolaire
                    classe.save()
                    return redirect('show_classe')
                except AnneScolaire.DoesNotExist:
                    form.add_error(None, "L'année scolaire sélectionnée n'existe pas.")
            else:
                form.add_error(None, "Veuillez sélectionner une année scolaire.")
    else:
        form = ClasseForm()
    
    return render(request, 'add_classe.html', {'form': form})
@login_required
def edit_classe(request, id):
    classe = get_object_or_404(Classe, id=id)

    if request.method == 'POST':
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            classe = form.save(commit=False)
            annee_scolaire_id = request.POST.get('annee_scolaire')

            # Vérifiez si l'ID est fourni et s'il correspond à une année scolaire
            if annee_scolaire_id:
                try:
                    annee_scolaire = AnneScolaire.objects.get(id=annee_scolaire_id)
                    classe.annee_scolaire = annee_scolaire
                    classe.save()
                    return redirect('show_classe')
                except AnneScolaire.DoesNotExist:
                    form.add_error(None, "L'année scolaire sélectionnée n'existe pas.")
            else:
                form.add_error(None, "Veuillez sélectionner une année scolaire.")
    else:
        form = ClasseForm(instance=classe)
    
    return render(request, 'edit_classe.html', {'form': form})

@login_required
def show_classe(request):
    annee_scolaire_id = request.GET.get('annee_scolaire')
    annees = AnneScolaire.objects.all()

    if annee_scolaire_id:
        selected_annee = get_object_or_404(AnneScolaire, id=annee_scolaire_id)
        classes = Classe.objects.filter(annee_scolaire=selected_annee)
    else:
        selected_annee = None
        classes = Classe.objects.none()  # Afficher aucun classe si aucune année n'est sélectionnée

    return render(request, 'show_classe.html', {
        'classes': classes,
        'annees': annees,
        'selected_annee': selected_annee
    })
@login_required
def edit_classe(request, id):
    classe = get_object_or_404(Classe, id=id)
    if request.method == 'POST':
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return redirect('show_classe')  # Redirige vers la vue affichant toutes les classes
    else:
        form = ClasseForm(instance=classe)
    return render(request, 'edit_classe.html', {'form': form})
@login_required
def delete_classe(request, id):
    classe = get_object_or_404(Classe, id=id)
    classe.delete()
    return redirect('show_classe')
@login_required
def add_matiere(request, classe_id=None):
    if request.method == "POST":
        form = MatiereForm(request.POST)
        if form.is_valid():
            matiere = form.save(commit=False)
            if classe_id:
                classe = get_object_or_404(Classe, id=classe_id)
                matiere.classe = classe
            matiere.save()
            return redirect('show_matiere_by_classe', classe_id=classe_id)  # Rediriger vers la liste des classes après l'ajout
    else:
        form = MatiereForm()

    context = {
        'form': form,
    }

    if classe_id:
        classe = get_object_or_404(Classe, id=classe_id)
        context['classe'] = classe

    return render(request, 'matieres/add_matiere.html', context)
@login_required
def add_matiere_by_classe(request):
    annee_scolaire_id = request.GET.get('annee_scolaire')
    
    if annee_scolaire_id:
        try:
            classes = Classe.objects.filter(annee_scolaire_id=annee_scolaire_id)
        except AnneScolaire.DoesNotExist:
            classes = Classe.objects.none()
    else:
        classes = Classe.objects.all()

    context = {
        'classes': classes,
        'annees': AnneScolaire.objects.all(),
        'selected_annee_id': annee_scolaire_id
    }
    return render(request, 'add_matiere_by_classe.html', context)
@login_required
def show_matiere_by_classe(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)
    matieres = Matiere.objects.filter(classe=classe)

    context = {
        'classe': classe,
        'matieres': matieres,
    }

    return render(request, 'matieres/show_matiere_by_classe.html', context)
@login_required
def delete_matiere(request, matiere_id):
    matiere = get_object_or_404(Matiere, id=matiere_id)
    classe_id = matiere.classe.id  # Assurez-vous que le modèle Matiere a un champ classe qui est une ForeignKey vers Classe
    matiere.delete()
    return redirect('show_matiere_by_classe', classe_id=classe_id)  # Remplacez par le nom correct de votre vue
@login_required
def edit_matiere(request, matiere_id):
    matiere = get_object_or_404(Matiere, id=matiere_id)
    if request.method == 'POST':
        form = MatiereForm(request.POST, instance=matiere)
        if form.is_valid():
            form.save()
            return redirect('/')  # Remplacez 'list_matieres' par le nom de votre vue de liste des matières
    else:
        form = MatiereForm(instance=matiere)

    return render(request, 'matieres/edit_matiere.html', {'form': form})

def show_list_eleve_by_classe(request):
    annee_scolaire_id = request.GET.get('annee_scolaire')

    if annee_scolaire_id:
        # Filtrer les classes par année scolaire sélectionnée
        classes = Classe.objects.filter(annee_scolaire_id=annee_scolaire_id)
    else:
        # Afficher toutes les classes si aucune année scolaire n'est sélectionnée
        classes = Classe.objects.all()

    # Passer les classes, les années scolaires et l'année sélectionnée au contexte
    context = {
        'classes': classes,
        'annees': AnneScolaire.objects.all(),
        'selected_annee_id': annee_scolaire_id
    }

    return render(request, 'show_list_eleve_by_classe.html', context)
@login_required
def add_eleve(request, classe_id=None):
    if request.method == "POST":
        form = EleveForm(request.POST, request.FILES)
        if form.is_valid():
            eleve = form.save(commit=False)
            if classe_id:
                classe = get_object_or_404(Classe, id=classe_id)
                eleve.classe = classe
            eleve.save()
            return redirect('show_eleves_by_class', classe_id = classe_id)
    else:
        form = EleveForm()
    
    context = {
        'form': form,
    }
    
    if classe_id:
        classe = get_object_or_404(Classe, id=classe_id)
        context['classe'] = classe

    return render(request, 'students/add_eleve.html', context)
@login_required
def show_eleves(request):
    eleves = Eleve.objects.all()
    return render(request, 'students/show_eleves.html', {'eleves': eleves})
@login_required
def show_eleves_by_class(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)
    eleves = Eleve.objects.filter(classe=classe)
    return render(request, 'students/show_eleves.html', {'eleves': eleves, 'classe': classe})
@login_required
def edit_eleve(request, id):
    eleve = Eleve.objects.get(id=id)
    classe_id = eleve.classe.id  # Extrait l'ID de la classe du professeur

    if request.method == "POST":
        form = EleveForm(request.POST, request.FILES, instance=eleve)
        if form.is_valid():
            form.save()
            return redirect('show_eleves_by_class', classe_id = classe_id)
    else:
        form = EleveForm(instance=eleve)
    return render(request, 'students/edit_eleve.html', {'form': form, 'eleve': eleve})
@login_required
def destroy_eleve(request, id):
    eleve = Eleve.objects.get(id=id)
    classe_id = eleve.classe.id 
    eleve.delete()
    return redirect('show_eleves_by_class', classe_id = classe_id)
@login_required
def detail_eleve(request, id):
    eleve = get_object_or_404(Eleve, id=id)
    return render(request, 'students/detail_eleve.html', {'eleve': eleve})
@login_required
def abscences_par_classe(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)
    eleves = Eleve.objects.filter(classe=classe)
    eleves_with_absences = []

    for eleve in eleves:
        nb_abscences = AbscenceEleve.objects.filter(eleve=eleve).count()
        eleves_with_absences.append({
            'id': eleve.id,
            'nom': eleve.nom,
            'prenom': eleve.prenom,
            'classe': eleve.classe.nom,
            'nb_absences': nb_abscences
        })

    context = {
        'classe': classe,
        'eleves': eleves_with_absences
    }
    return render(request, 'students/abscence/show.html', context)
@login_required
def ajouter_abscence(request, id):
    eleve = get_object_or_404(Eleve, id=id)
    if request.method == 'POST':
        form = AbscenceEleveForm(request.POST)
        if form.is_valid():
            abscence = form.save(commit=False)
            abscence.eleve = eleve
            classe_id = eleve.classe.id

            abscence.save()
            return redirect('detail_abscence', id = eleve.id)
    else:
        form = AbscenceEleveForm()

    context = {
        'form': form,
        'eleve': eleve,
    }
    return render(request, 'students/abscence/ajouter_abscence.html', context)
@login_required
def detail_abscence(request, id):
    eleve = get_object_or_404(Eleve, id=id)
    abscences = AbscenceEleve.objects.filter(eleve=eleve)
    context = {
        'eleve': eleve,
        'abscences': abscences
    }
    return render(request, 'students/abscence/detail.html', context)
@login_required
def edit_abscence(request, id):
    abscence = get_object_or_404(AbscenceEleve, id=id)
    eleve_id = abscence.eleve.id
    if request.method == 'POST':
        form = AbscenceEleveForm(request.POST, instance=abscence)
        if form.is_valid():
            form.save()
            return redirect('detail_abscence', id=eleve_id)
    else:
        form = AbscenceEleveForm(instance=abscence)
    
    context = {
        'form': form,
        'abscence': abscence,
    }
    return render(request, 'students/abscence/edit.html', context)
@login_required
def delete_abscence(request, id):
    abscence = get_object_or_404(AbscenceEleve, id=id)
    eleve_id = abscence.eleve.id
    abscence.delete()
    return redirect('detail_abscence', id=eleve_id)
@login_required
def show_abscence_by_classe(request):
    annee_scolaire_id = request.GET.get('annee_scolaire')

    if annee_scolaire_id:
        # Filtrer les classes par année scolaire sélectionnée
        classes = Classe.objects.filter(annee_scolaire_id=annee_scolaire_id)
    else:
        # Afficher toutes les classes si aucune année scolaire n'est sélectionnée
        classes = Classe.objects.all()

    # Passer les classes, les années scolaires et l'année sélectionnée au contexte
    context = {
        'classes': classes,
        'annees': AnneScolaire.objects.all(),
        'selected_annee_id': annee_scolaire_id
    }
    return render(request, 'show_abscence_by_classe.html',context)
@login_required
def add_controle(request, classe_id=None):
    if request.method == "POST":
        form = ControleForm(request.POST)
        if form.is_valid():
            controle = form.save(commit=False)
            if classe_id:
                classe = get_object_or_404(Classe, id=classe_id)
                controle.classe = classe
            controle.save()
            return redirect('show_controle_by_classe', classe_id=classe_id)
    else:
        form = ControleForm()

    context = {
        'form': form,
    }

    if classe_id:
        classe = get_object_or_404(Classe, id=classe_id)
        context['classe'] = classe

    return render(request, 'controles/add_controle.html', context)
@login_required
def show_controle_by_classe(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)
    controles = Controle.objects.filter(matiere__classe=classe)

    context = {
        'classe': classe,
        'controles': controles,
    }
    return render(request, 'controles/show_controle_by_classe.html', context)
@login_required
def edit_controle(request, id):
    controle = get_object_or_404(Controle, id=id)
    classe_id = controle.matiere.classe.id
    if request.method == 'POST':
        form = ControleForm(request.POST, instance=controle)
        if form.is_valid():
            form.save()
            return redirect('show_controle_by_classe', classe_id=classe_id)
    else:
        form = ControleForm(instance=controle)
    
    context = {
        'form': form,
        'controle': controle,
    }
    return render(request, 'controles/edit_controle.html', context)
@login_required
def delete_controle(request, id):
    controle = get_object_or_404(Controle, id=id)
    matiere = controle.matiere
    classe_id = matiere.classe.id  # Utilisez la classe associée à la matière
    controle.delete()
    return redirect('show_controle_by_classe', classe_id=classe_id)
@login_required
def add_notes_for_all_students(request, controle_id):
    controle = get_object_or_404(Controle, id=controle_id)
    students = Eleve.objects.filter(classe=controle.matiere.classe)
    controle_id = controle.matiere.classe.id  # Correction ici

    # Create the formset with the updated form
    NoteFormSet = modelformset_factory(Note, form=NoteForm, extra=len(students))

    if request.method == 'POST':
        formset = NoteFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                note = form.save(commit=False)
                note.controle = controle
                note.save()
            return redirect('students_notes', controle_id = controle_id)  # Change 'success_view' to the name of your success view
    else:
        initial_data = [{'eleve': student} for student in students]
        formset = NoteFormSet(queryset=Note.objects.none(), initial=initial_data)

    return render(request, 'note/add_note.html', {'formset': formset, 'controle': controle})
@login_required
def edit_note_view(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('students_notes', controle_id=note.controle.id)  # Redirection vers la page des notes
    else:
        form = NoteForm(instance=note)
    return render(request, 'note/edit_note.html', {'form': form, 'note': note})
@login_required
def delete_note(request, note_id):
    # Récupérer l'objet Note à supprimer
    note = get_object_or_404(Note, id=note_id)
    
    # Récupérer l'objet Controle associé à la Note
    controle = note.controle
    
    # Supprimer la Note
    note.delete()
    
    # Rediriger vers la page des notes associées à ce contrôle
    return redirect('students_notes', controle_id=controle.id)
@login_required
def students_notes(request, controle_id):
    controle = get_object_or_404(Controle, id=controle_id)
    notes = Note.objects.filter(controle=controle).select_related('eleve')

    context = {
        'controle': controle,
        'notes': notes,
    }
    return render(request, 'note/students_notes.html', context)
@login_required
def show_notes(request):
    annee_scolaire_id = request.GET.get('annee_scolaire')

    if annee_scolaire_id:
        # Filtrer les classes par année scolaire sélectionnée
        classes = Classe.objects.filter(annee_scolaire_id=annee_scolaire_id)
    else:
        # Afficher toutes les classes si aucune année scolaire n'est sélectionnée
        classes = Classe.objects.all()

    # Passer les classes, les années scolaires et l'année sélectionnée au contexte
    context = {
        'classes': classes,
        'annees': AnneScolaire.objects.all(),
        'selected_annee_id': annee_scolaire_id
    }
    return render(request, 'note/show_note.html',context)
@login_required
def show_notes_by_classe(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)
    eleves = Eleve.objects.filter(classe=classe)
    matieres = Matiere.objects.filter(classe=classe)

    context = {
        'classe': classe,
        'eleves': eleves,
        'matieres': matieres,
    }

    return render(request, 'note/show_note_by_classe.html', context)

# ******gestion professeur******
# Ajouter un professeur
@login_required
def add_professeur(request, classe_id=None):
    # Récupère la classe si l'ID est fourni
    classe = None
    if classe_id:
        classe = get_object_or_404(Classe, id=classe_id)
        
    if request.method == 'POST':
        form = ProfesseurForm(request.POST, request.FILES)
        if form.is_valid():
            professeur = form.save(commit=False)
            if classe:
                professeur.classe = classe
            professeur.save()
            return redirect('show_professeur_by_classe', classe_id=classe_id)
    else:
        form = ProfesseurForm()

    context = {'form': form}
    if classe:
        context['classe'] = classe
    
    return render(request, 'teachers/add_teacher.html', context)
@login_required
def show_list_professeur_by_classe(request):
    annee_scolaire_id = request.GET.get('annee_scolaire')

    if annee_scolaire_id:
        # Filtrer les classes par année scolaire sélectionnée
        classes = Classe.objects.filter(annee_scolaire_id=annee_scolaire_id)
    else:
        # Afficher toutes les classes si aucune année scolaire n'est sélectionnée
        classes = Classe.objects.all()

    # Passer les classes, les années scolaires et l'année sélectionnée au contexte
    context = {
        'classes': classes,
        'annees': AnneScolaire.objects.all(),
        'selected_annee_id': annee_scolaire_id
    }
    return render(request, 'show_list_professeur_by_classe.html', context)
@login_required
def show_professeur(request):
    professeur = Professeur.objects.all()
    return render(request, 'teachers/show_teacher.html', {'professeur': professeur})

# Afficher les professeurs par classe
@login_required
def show_professeur_by_classe(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)
    professeurs = Professeur.objects.filter(classe=classe)
    return render(request, 'teachers/show_teacher.html', {'professeurs': professeurs, 'classe': classe})

# Éditer un professeur
@login_required
def edit_professeur(request, id):
    professeur = Professeur.objects.get(id=id)
    classe_id = professeur.classe.id  # Extrait l'ID de la classe du professeur
    if request.method == 'POST':
        form = ProfesseurForm(request.POST, request.FILES, instance=professeur)
        if form.is_valid():
            form.save()
            return redirect('show_professeur_by_classe', classe_id=classe_id)
    else:
        form = ProfesseurForm(instance=professeur)
    return render(request, 'teachers/edit_teacher.html', {'form': form, 'professeur': professeur})

# Supprimer un professeur
@login_required
def delete_professeur(request, id):
    professeur = get_object_or_404(Professeur, id=id)
    classe_id = professeur.classe.id  # Extrait l'ID de la classe du professeur
    professeur.delete()
    return redirect('show_professeur_by_classe', classe_id=classe_id)
#detail professeur
@login_required
def detail_professeur(request, id):
    professeur = get_object_or_404(Professeur, id=id)
    return render(request, 'teachers/detail_teacher.html', {'professeur': professeur})

#*********Abscence*********
@login_required
def abscences_prof_par_classe(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)
    professeurs = Professeur.objects.filter(classe=classe)
    professeurs_with_absences = []

    for professeur in professeurs:
        nb_abscences = AbscenceProfesseur.objects.filter(professeur=professeur).count()
        professeurs_with_absences.append({
            'id': professeur.id,
            'nom': professeur.nom,
            'prenom': professeur.prenom,
            'classe': professeur.classe.nom,
            'nb_absences': nb_abscences
        })

    context = {
        'classe': classe,
        'professeurs': professeurs_with_absences
    }
    return render(request, 'teachers/abscence/show.html', context)
@login_required
def ajouter_abscence_prof(request, id):
    professeur = get_object_or_404(Professeur, id=id)
    if request.method == 'POST':
        form = AbscenceProfesseurForm(request.POST)
        if form.is_valid():
            abscence = form.save(commit=False)
            abscence.professeur = professeur
            abscence.save()
            return redirect('detail_abscence_prof', id = professeur.id)
    else:
        form = AbscenceProfesseurForm()

    context = {
        'form': form,
        'professeur': professeur,
    }
    return render(request, 'teachers/abscence/ajouter_abscence.html', context)
@login_required
def detail_abscence_prof(request, id):
    professeur = get_object_or_404(Professeur, id=id)
    abscences = AbscenceProfesseur.objects.filter(professeur=professeur)
    context = {
        'professeur': professeur,
        'abscences': abscences
    }
    return render(request, 'teachers/abscence/detail.html', context)
@login_required
def edit_abscence_prof(request, id):
    abscence = get_object_or_404(AbscenceProfesseur, id=id)
    if request.method == 'POST':
        form = AbscenceProfesseurForm(request.POST, instance=abscence)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AbscenceProfesseurForm(instance=abscence)
    
    context = {
        'form': form,
        'abscence': abscence,
    }
    return render(request, 'teachers/abscence/edit.html', context)
@login_required
def delete_abscence_prof(request, id):
    abscence = get_object_or_404(AbscenceProfesseur, id=id)
    abscence_prof_id = abscence.professeur.id  # Utilisez l'attribut 'professeur' de l'absence
    abscence.delete()
    return redirect('detail_abscence_prof', id = abscence_prof_id)
@login_required
def show_abscence_prof_by_classe(request):
    annee_scolaire_id = request.GET.get('annee_scolaire')

    if annee_scolaire_id:
        # Filtrer les classes par année scolaire sélectionnée
        classes = Classe.objects.filter(annee_scolaire_id=annee_scolaire_id)
    else:
        # Afficher toutes les classes si aucune année scolaire n'est sélectionnée
        classes = Classe.objects.all()

    # Passer les classes, les années scolaires et l'année sélectionnée au contexte
    context = {
        'classes': classes,
        'annees': AnneScolaire.objects.all(),
        'selected_annee_id': annee_scolaire_id
    }
    return render(request, 'show_abscence_prof_by_classe.html',context)

#*******emploi du temp********
@login_required
def show_emplois_du_temps(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)
    emplois_du_temps = EmploiDuTemps.objects.filter(classe=classe)
    return render(request, 'calendrier/emploi_du_temps/emploi_du_temps.html', {'classe': classe, 'emplois_du_temps': emplois_du_temps})
@login_required
def show_emplois_du_temps_by_classe(request):
    annee_scolaire_id = request.GET.get('annee_scolaire')

    if annee_scolaire_id:
        # Filtrer les classes par année scolaire sélectionnée
        classes = Classe.objects.filter(annee_scolaire_id=annee_scolaire_id)
    else:
        # Afficher toutes les classes si aucune année scolaire n'est sélectionnée
        classes = Classe.objects.all()

    # Passer les classes, les années scolaires et l'année sélectionnée au contexte
    context = {
        'classes': classes,
        'annees': AnneScolaire.objects.all(),
        'selected_annee_id': annee_scolaire_id
    }
    return render(request, 'show_emploi_du_temps_by_classe.html',context)
@login_required
def add_emploi_du_temps(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)
    if request.method == 'POST':
        form = EmploiDuTempsForm(request.POST, request.FILES)
        if form.is_valid():
            emploi_du_temps = form.save(commit=False)
            emploi_du_temps.classe = classe
            emploi_du_temps.save()
            return redirect('show_emplois_du_temps', classe_id=classe.id)
    else:
        form = EmploiDuTempsForm()
    return render(request, 'calendrier/emploi_du_temps/add_emploi_du_temps.html', {'form': form, 'classe': classe})

@login_required
def delete_emploi_du_temps(request, emploi_id):
    emploi_du_temps = get_object_or_404(EmploiDuTemps, id=emploi_id)
    classe_id = emploi_du_temps.classe.id
    emploi_du_temps.delete()
    return redirect('show_emplois_du_temps', classe_id=classe_id)

@login_required
def edit_emploi_du_temps(request, emploi_id):
    emploi_du_temps = get_object_or_404(EmploiDuTemps, id=emploi_id)
    if request.method == 'POST':
        form = EmploiDuTempsForm(request.POST, request.FILES, instance=emploi_du_temps)
        if form.is_valid():
            form.save()
            return redirect('show_emplois_du_temps', classe_id=emploi_du_temps.classe.id)
    else:
        form = EmploiDuTempsForm(instance=emploi_du_temps)
    return render(request, 'calendrier/emploi_du_temps/edit_emploi_du_temps.html', {'form': form, 'emploi_du_temps': emploi_du_temps})

#*********composition********
@login_required
def show_composition(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)
    composition = Composition.objects.filter(classe=classe)
    return render(request, 'calendrier/composition/composition.html', {'classe': classe, 'composition': composition})

@login_required
def show_composition_by_classe(request):
    annee_scolaire_id = request.GET.get('annee_scolaire')

    if annee_scolaire_id:
        # Filtrer les classes par année scolaire sélectionnée
        classes = Classe.objects.filter(annee_scolaire_id=annee_scolaire_id)
    else:
        # Afficher toutes les classes si aucune année scolaire n'est sélectionnée
        classes = Classe.objects.all()

    # Passer les classes, les années scolaires et l'année sélectionnée au contexte
    context = {
        'classes': classes,
        'annees': AnneScolaire.objects.all(),
        'selected_annee_id': annee_scolaire_id
    }
    return render(request, 'show_composition_by_classe.html',context)

@login_required
def add_composition(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)
    if request.method == 'POST':
        form = CompositionForm(request.POST, request.FILES)
        if form.is_valid():
            composition = form.save(commit=False)
            composition.classe = classe
            composition.save()
            return redirect('show_composition', classe_id=classe.id)
    else:
        form = EmploiDuTempsForm()
    return render(request, 'calendrier/composition/add_composition.html', {'form': form, 'classe': classe})

@login_required
def delete_composition(request, composition_id):
    composition = get_object_or_404(Composition, id=composition_id)
    classe_id = composition.classe.id
    composition.delete()
    return redirect('show_composition', classe_id=classe_id)

@login_required
def edit_composition(request, composition_id):
    composition = get_object_or_404(Composition, id=composition_id)
    if request.method == 'POST':
        form = CompositionForm(request.POST, request.FILES, instance=composition)
        if form.is_valid():
            form.save()
            return redirect('show_composition', classe_id=composition.classe.id)
    else:
        form = CompositionForm(instance=composition)
    return render(request, 'calendrier/composition/edit_composition.html', {'form': form, 'composition': composition})


@login_required
def mes_notes(request):
    user = request.user

    if not user.is_student:
        # Redirection vers la page d'accueil si l'utilisateur n'est pas un étudiant
        return redirect('login_view')
    
    # Récupérer l'élève associé à l'utilisateur
    eleve = get_object_or_404(Eleve, user=user)

    # Récupérer les notes de l'élève connecté
    notes = Note.objects.filter(eleve=eleve)
    
    return render(request, 'note/mes_notes.html', {'notes': notes})

@login_required
def mes_informations(request):
    # Récupérer l'élève associé à l'utilisateur
    eleve = get_object_or_404(Eleve, user=request.user)
    
    return render(request, 'students/mes_information.html', {'eleve': eleve})

@login_required
def mes_abscences(request):
    user = request.user

    if not user.is_student:
        # Rediriger ou afficher un message d'erreur si l'utilisateur n'est pas un élève
        return redirect('home')

    # Assurez-vous que l'utilisateur a un élève associé
    eleve = get_object_or_404(Eleve, user=user)

    # Récupérer les absences de l'élève connecté
    absences = AbscenceEleve.objects.filter(eleve=eleve)

    return render(request, 'students/abscence/mes_abscences.html', {'absences': absences, 'classe': eleve.classe})

@login_required
def emploi_du_temps_eleve(request):
    user = request.user

    if user.is_student:
        # L'utilisateur est un élève
        eleve = get_object_or_404(Eleve, user=user)
        emplois_du_temps = EmploiDuTemps.objects.filter(classe=eleve.classe)
        return render(request, 'calendrier/emploi_du_temps/emploi_du_temps_eleve.html', {
            'classe': eleve.classe,
            'emplois_du_temps': emplois_du_temps
        })

    elif user.is_teacher:
        # L'utilisateur est un professeur
        professeur = Professeur.objects.get(user_username=user.username)
        emplois_du_temps = EmploiDuTemps.objects.filter(classe=professeur.classe)
        return render(request, 'calendrier/emploi_du_temps/emploi_du_temps_eleve.html', {
            'emplois_du_temps': emplois_du_temps, 
            'classe': professeur.classe
        })
    else:
        # L'utilisateur n'est ni un élève ni un professeur, redirection ou message d'erreur
        return redirect('home')
    
@login_required
def compositions_eleve(request):
    user = request.user

    if user.is_student:
        # L'utilisateur est un élève
        eleve = get_object_or_404(Eleve, user=user)
        compositions = Composition.objects.filter(classe=eleve.classe)
        return render(request, 'calendrier/composition/students_compositions.html', {
            'compositions': compositions, 
            'classe': eleve.classe
        })

    elif user.is_teacher:
        # L'utilisateur est un professeur
        professeur = Professeur.objects.get(user_username=user.username)
        compositions = Composition.objects.filter(classe=professeur.classe)
        return render(request, 'calendrier/composition/students_compositions.html', {
            'compositions': compositions, 
            'classe': professeur.classe
        })
    else:
        # L'utilisateur n'est ni un élève ni un professeur, redirection ou message d'erreur
        return redirect('home')
    
@login_required
def list_eleves_professeur(request):
    # Assurez-vous que l'utilisateur est un professeur
    if not request.user.is_teacher:
        return redirect('dashboard')

    # Récupérer le professeur associé à l'utilisateur connecté
    try:
        professeur = Professeur.objects.get(user_username=request.user.username)
    except Professeur.DoesNotExist:
        return redirect('dashboard')

    # Récupérer la classe du professeur
    classe = professeur.classe

    # Filtrer les élèves en fonction de cette classe
    eleves = Eleve.objects.filter(classe=classe)

    context = {
        'eleves': eleves,
    }

    return render(request, 'teachers/liste_eleve_prof.html', context)


@login_required
def show_professeur_matieres(request):
    # Assurez-vous que l'utilisateur est un professeur
    if not request.user.is_teacher:
        return redirect('dashboard')

    # Récupérer le professeur associé à l'utilisateur connecté
    try:
        professeur = Professeur.objects.get(user_username=request.user.username)
    except Professeur.DoesNotExist:
        return redirect('dashboard')

    # Récupérer la classe du professeur
    classe = professeur.classe

    # Si le professeur est associé à une classe, récupère les matières de cette classe
    if classe:
        matieres = Matiere.objects.filter(classe=classe)
    else:
        matieres = Matiere.objects.none()

    context = {
        'classe': classe,
        'matieres': matieres,
    }

    return render(request, 'teachers/professeur_matieres.html', context)



@login_required
def show_professeur_info(request):
    # Récupérer le professeur connecté
    professeur = get_object_or_404(Professeur, user_username=request.user.username)
    
    # Récupérer la classe du professeur
    classe = professeur.classe

    # Récupérer les matières associées à la classe
    if classe:
        matieres = Matiere.objects.filter(classe=classe)
    else:
        matieres = Matiere.objects.none()

    context = {
        'professeur': professeur,
        'classe': classe,
        'matieres': matieres,
    }

    return render(request, 'teachers/professeur_info.html', context)