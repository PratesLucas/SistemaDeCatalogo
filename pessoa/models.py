from django.db import models
from accounts.models import Usuario

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.nome


class ArquivoPDF(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='arquivos')
    pdf = models.FileField(upload_to='pdfs/')