# Generated by Django 5.0.2 on 2024-08-09 16:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnneScolaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.CharField(help_text="Année scolaire au format '2023-2024'", max_length=10, unique=True)),
                ('date_debut', models.DateField(help_text="Date de début de l'année scolaire")),
                ('date_fin', models.DateField(help_text="Date de fin de l'année scolaire")),
                ('actif', models.BooleanField(default=True, help_text="Indique si l'année scolaire est actuellement active")),
            ],
            options={
                'verbose_name': 'Année Scolaire',
                'verbose_name_plural': 'Années Scolaires',
            },
        ),
        migrations.RemoveField(
            model_name='eleve',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='eleve',
            name='user_password',
        ),
        migrations.RemoveField(
            model_name='eleve',
            name='user_username',
        ),
        migrations.AddField(
            model_name='eleve',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='eleve', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classe',
            name='annee_scolaire',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='students.annescolaire'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='photos/')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='composition', to='students.classe')),
            ],
        ),
        migrations.CreateModel(
            name='EmploiDuTemps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='photos/')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emplois_du_temps', to='students.classe')),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matieres', to='students.classe')),
            ],
            options={
                'db_table': 'tblmatieres',
            },
        ),
        migrations.CreateModel(
            name='Controle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('Devoir', 'Devoir'), ('Examen', 'Examen')], max_length=20)),
                ('description', models.TextField(blank=True)),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='controles', to='students.matiere')),
            ],
            options={
                'db_table': 'tblcontroles',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.DecimalField(decimal_places=2, max_digits=5)),
                ('controle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='students.controle')),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='students.eleve')),
            ],
            options={
                'db_table': 'tblnotes',
            },
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_naissance', models.DateField()),
                ('sexe', models.CharField(choices=[('masculin', 'Masculin'), ('feminin', 'Feminin')], max_length=10)),
                ('lieu_naissance', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=15)),
                ('photo_profil', models.ImageField(upload_to='photos')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professeurs', to='students.classe')),
            ],
        ),
        migrations.CreateModel(
            name='AbscenceProfesseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2000-02-02')),
                ('type', models.CharField(choices=[('Justifier', 'Justifier'), ('Non-justifier', 'Non-justifier')], default='Non-justifier', max_length=20)),
                ('professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abscences', to='students.professeur')),
            ],
            options={
                'db_table': 'tblabsencesprofesseurs',
                'ordering': ['date'],
            },
        ),
    ]
