from django import forms
from teachers.models import Professeur

class ProfesseurForm(forms.ModelForm):
    class Meta:
        model = Professeur
        fields = ['nom', 'prenom', 'cin_professeur', 'sexe', 'date_naissance', 'lieu_naissance', 'photo_profil','niveau_enseignement']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'cin_professeur': forms.TextInput(attrs={'class': 'form-control'}),
            'sexe': forms.Select(attrs={'class': 'form-control'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lieu_naissance': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_profil': forms.FileInput(attrs={'class': 'form-control-file'}),
            'niveau_enseignement': forms.TextInput(attrs={'class': 'form-control'}),
        }
