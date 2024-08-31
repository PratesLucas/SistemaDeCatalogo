from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=50)
