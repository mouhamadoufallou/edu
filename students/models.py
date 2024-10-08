from django.db import models
from datetime import date
from django.contrib.auth.models import User
import random, string
from django.conf import settings  # Import settings to use the custom user model
from accounts.models import User as CustomUser
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model



def generate_random_password(length=3):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))
class AnneScolaire(models.Model):
    annee = models.CharField(max_length=10, unique=True, help_text="Année scolaire au format '2023-2024'")
    date_debut = models.DateField(help_text="Date de début de l'année scolaire")
    date_fin = models.DateField(help_text="Date de fin de l'année scolaire")
    actif = models.BooleanField(default=True, help_text="Indique si l'année scolaire est actuellement active")

    def __str__(self):
        return self.annee

    class Meta:
        verbose_name = "Année Scolaire"
        verbose_name_plural = "Années Scolaires"
class Classe(models.Model):
    nom = models.CharField(max_length=100)
    annee_scolaire = models.ForeignKey(AnneScolaire, on_delete=models.CASCADE)
    class Meta:
        db_table = "tblclasses"
    def __str__(self):
        return self.nom
    
CustomUser = get_user_model()
class Eleve(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='eleve')
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    cin_eleve = models.CharField(max_length=20, unique=True)
    sexe_choice = (
        ("masculin", "Masculin"),
        ("feminin", "Feminin"),
    )
    sexe = models.CharField(choices=sexe_choice, max_length=10)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    photo_profil = models.ImageField(upload_to='photos')
    date_admission = models.DateField()
    classe = models.ForeignKey('Classe', on_delete=models.SET_NULL, null=True, blank=True)
    niveau_scolaire = models.CharField(max_length=50)
    nom_parent = models.CharField(max_length=100)
    prenom_parent = models.CharField(max_length=100)
    date_naissance_parent = models.DateField()
    lieu_naissance_parent = models.CharField(max_length=100)
    tel_parent = models.CharField(max_length=20)
    user_username = models.CharField(max_length=150, blank=True, null=True)
    user_email = models.EmailField(blank=True, null=True)
    user_password = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = "tblstudents"

    def save(self, *args, **kwargs):
        # Si l'utilisateur n'est pas encore associé, le créer
        if not self.user_id:
            base_username = f"{self.nom.lower()}"
            username = base_username
            email = f"{username}@example.com"
            password = get_random_string(8)

            # Vérifier que le nom d'utilisateur est unique
            user_exists = CustomUser.objects.filter(username=username).exists()
            suffix = 1
            while user_exists:
                username = f"{base_username}{suffix}"
                user_exists = CustomUser.objects.filter(username=username).exists()
                suffix += 1

            # Créer l'utilisateur
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.is_student = True
            user.save()

            # Associer l'utilisateur à l'élève
            self.user = user
            self.user_username = username
            self.user_email = email
            self.user_password = password

        super(Eleve, self).save(*args, **kwargs)

        # Créer une absence par défaut si l'élève est nouvellement créé
        if not self.pk:
            AbscenceEleve.objects.create(eleve=self, type='non-justifiée')
                        
class AbscenceEleve(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='abscences')
    date = models.DateField(default='2000-02-02')
    type_choices = (("Justifier", "Justifier"),
                    ("Non-justifier", "Non-justifier"))
    type = models.CharField(max_length=20, choices=type_choices, default='Non-justifier')

    def update_absence(self, date, type):
        self.date = date
        self.type = type
        self.save()

    class Meta:
        db_table = "tblabsenceseleves"
        ordering = ['date']

    def __str__(self):
        return f"{self.eleve.nom} {self.eleve.prenom} - {self.date} - {self.type}"

class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='matieres')

    class Meta:
        db_table = "tblmatieres"
    def __str__(self):
        return self.nom

class Controle(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='controles')
    date = models.DateField()
    type_choices = (
        ("Devoir", "Devoir"),
        ("Examen", "Examen")
    )
    type = models.CharField(max_length=20, choices=type_choices)  # Retirez la virgule ici
    description = models.TextField(blank=True)

    class Meta:
        db_table = "tblcontroles"

    def __str__(self):
        return f"{self.matiere.nom} - {self.date}"


class Note(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='notes')
    controle = models.ForeignKey(Controle, on_delete=models.CASCADE, related_name='notes')
    note = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "tblnotes"

    def __str__(self):
        return f"{self.eleve.prenom} {self.eleve.nom} - {self.controle.matiere.nom}: {self.note}"


class Professeur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    sexe_choice = (
        ("masculin", "Masculin"),
        ("feminin", "Feminin"),
    )
    sexe = models.CharField(choices=sexe_choice, max_length=10)
    lieu_naissance = models.CharField(max_length=100)
    tel = models.CharField(max_length=15)
    photo_profil = models.ImageField(upload_to='photos')
    classe = models.ForeignKey('Classe', on_delete=models.CASCADE, related_name='professeurs')

    # Champs pour stocker les informations de l'utilisateur associé
    user_username = models.CharField(max_length=150, blank=True, null=True)
    user_email = models.EmailField(blank=True, null=True)
    user_password = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Vérifie si l'objet est nouvellement créé
            base_username = f"{self.nom.lower()}"
            username = base_username
            email = f"{username}@example.com"
            password = get_random_string(8)

            # Vérifier que le nom d'utilisateur est unique
            user_exists = CustomUser.objects.filter(username=username).exists()
            suffix = 1
            while user_exists:
                username = f"{base_username}{suffix}"
                user_exists = CustomUser.objects.filter(username=username).exists()
                suffix += 1

            # Créer l'utilisateur
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.is_teacher = True
            user.save()

            # Mettre à jour les informations de l'utilisateur dans Professeur
            self.user_username = username
            self.user_email = email
            self.user_password = password

        super(Professeur, self).save(*args, **kwargs)

        # Créer une absence par défaut si le professeur est nouvellement créé
        if not self.pk:
            AbscenceProfesseur.objects.create(professeur=self, type='non-justifiée')

    
class AbscenceProfesseur(models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE, related_name='abscences')
    date = models.DateField(default='2000-02-02')
    type_choices = (("Justifier", "Justifier"),
                    ("Non-justifier", "Non-justifier"))
    type = models.CharField(max_length=20, choices=type_choices, default='Non-justifier')

    def update_absence(self, date, type):
        self.date = date
        self.type = type
        self.save()

    class Meta:
        db_table = "tblabsencesprofesseurs"
        ordering = ['date']
class EmploiDuTemps(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='emplois_du_temps')
    img = models.ImageField(upload_to='photos/')
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"Emploi du temps de {self.classe.nom} du {self.date_debut} au {self.date_fin}"
    
class Composition(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='composition')
    img = models.ImageField(upload_to='photos/')
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"Composition de le classe de {self.classe.nom} du {self.date_debut} au {self.date_fin}"