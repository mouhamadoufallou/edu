# Generated by Django 5.0.2 on 2024-08-15 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_professeur_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professeur',
            name='user',
        ),
    ]
