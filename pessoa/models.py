from django.db import models
from accounts.models import Usuario

class Pessoa(Usuario):
    idade = models.IntegerField()
    rg = models.CharField(max_length=14)