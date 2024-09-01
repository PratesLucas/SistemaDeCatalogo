from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    TIPO_CHOICES = [("SECRETARIO", "Secretário"), ("DIRETOR", "Diretor")]
    
    cpf = models.CharField(max_length=11, unique=True)