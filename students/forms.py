from django import forms
from .models import *
from django.forms import modelformset_factory

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = [
            'nom', 'prenom', 'cin_eleve', 'sexe', 'date_naissance', 'lieu_naissance',
            'photo_profil', 'date_admission', 'niveau_scolaire',
            'nom_parent', 'prenom_parent', 'date_naissance_parent',
            'lieu_naissance_parent', 'tel_parent'
        ]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'cin_eleve': forms.TextInput(attrs={'class': 'form-control'}),
            'sexe': forms.Select(attrs={'class': 'form-control'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lieu_naissance': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_profil': forms.FileInput(attrs={'class': 'form-control-file'}),
            'date_admission': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'niveau_scolaire': forms.TextInput(attrs={'class': 'form-control'}),
            'nom_parent': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom_parent': forms.TextInput(attrs={'class': 'form-control'}),
            'date_naissance_parent': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lieu_naissance_parent': forms.TextInput(attrs={'class': 'form-control'}),
            'tel_parent': forms.TextInput(attrs={'class': 'form-control'}),
        }
class AbscenceEleveForm(forms.ModelForm):
    class Meta:
        model = AbscenceEleve
        fields = ['date', 'type']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }
class ClasseForm(forms.ModelForm):
    annee_scolaire = forms.ModelChoiceField(
        queryset=AnneScolaire.objects.all(), 
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Classe
        fields = ['nom', 'annee_scolaire']  # Incluez 'annee_scolaire' ici
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
        }
class ControleForm(forms.ModelForm):
    class Meta:
        model = Controle
        fields = ['date', 'type', 'description', 'matiere']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'matiere': forms.Select(attrs={'class': 'form-control'}),
        }


class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = ['nom']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['eleve', 'note']
        widgets = {
            'note': forms.NumberInput(attrs={'class': 'form-control'}),
            'eleve': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        # Customizing the label of the select field to show the student's name
        self.fields['eleve'].queryset = Eleve.objects.all()
        self.fields['eleve'].label_from_instance = lambda obj: f"{obj.nom} {obj.prenom}"
        
class ProfesseurForm(forms.ModelForm):
    class Meta:
        model = Professeur
        fields = ['nom', 'prenom', 'date_naissance', 'lieu_naissance', 'tel', 'photo_profil', 'sexe']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lieu_naissance': forms.TextInput(attrs={'class': 'form-control'}),
            'sexe': forms.Select(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_profil': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
class AbscenceProfesseurForm(forms.ModelForm):
    class Meta:
        model = AbscenceProfesseur
        fields = ['date', 'type']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }
class EmploiDuTempsForm(forms.ModelForm):
    class Meta:
        model = EmploiDuTemps
        fields = ['img', 'date_debut', 'date_fin']
        widgets = {
            'img': forms.FileInput(attrs={'class': 'form-control-file'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

        }
class CompositionForm(forms.ModelForm):
    class Meta:
        model = Composition
        fields = ['img', 'date_debut', 'date_fin']
        widgets = {
            'img': forms.FileInput(attrs={'class': 'form-control-file'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

        }
class AnneScolaireForm(forms.ModelForm):
    class Meta:
        model = AnneScolaire
        fields = ['annee', 'date_debut', 'date_fin', 'actif']
        widgets = {
            'annee': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'actif': forms.CheckboxInput(attrs={'class': 'form-control-file'}),
        }