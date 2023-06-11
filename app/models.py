from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLES = (('adm', 'admin'), ('prof', 'profesor'), ('stu', 'student'))
    STATUS = (('none', 'None'), ('izv', 'izvanredni student'), ('red', 'redovni student'))
    role = models.CharField(max_length=50, choices=ROLES)
    status = models.CharField(max_length=50, choices=STATUS)

class Course(models.Model):
    OPTIONAL_CHOICES = (('DA', 'da'), ('NE', 'ne'))
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    ects = models.IntegerField()
    sem_red = models.IntegerField()
    sem_izv = models.IntegerField()
    optional = models.CharField(max_length=50, choices=OPTIONAL_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, limit_choices_to = {'role' : 'prof'}, null=True)