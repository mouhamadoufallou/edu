from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_student = models.BooleanField('Is student', default=False)
    is_teacher = models.BooleanField('Is teacher', default=False)