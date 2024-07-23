from django.db import models

# Create your models here.
class Professeur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    cin_professeur = models.CharField(max_length=20, unique=True)
    sexe_choice = (
        ("masculin", "Masculin"),
        ("feminin", "Feminin"),
    )
    sexe = models.CharField(choices=sexe_choice, max_length=10)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    photo_profil = models.ImageField(upload_to='photos')
    niveau_enseignement = models.CharField(max_length=100)

    class Meta:  
        db_table = "tblprofesseur"