from django.db import models
from accounts.models import Usuario

class Pessoa(Usuario):
    idade = models.IntegerField()
    rg = models.CharField(max_length=14)

    def __str__(self):
        return f"Ata {self.nome} - {self.idade} - {self.rg}"