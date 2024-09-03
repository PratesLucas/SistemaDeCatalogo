from django.db import models
from accounts.models import Usuario


class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    num = models.DecimalField(max_digits=5, decimal_places=0)
    complemento = models.TextField()
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    estado = models.CharField(max_length=2)


class Pessoa(models.Model):
    TIPOS_PESSOAS_DICT = {
        "ALUNO": "aluno",
        "PROFESSOR": "professor",
    }
    TIPOS_PESSOAS = [
        ("ALUNO", "aluno"),
        ("PROFESSOR", "professor"),
    ]
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    pdf = models.FileField(upload_to='pdfs/')
    tipo_pessoa = models.CharField("tipo de pessoa",max_length=10, choices= TIPOS_PESSOAS, default= "ALUNO" )
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, related_name='pessoas', blank=True, null=True, default=None)   

    def __str__(self):
        return self.nome


class ArquivoPDF(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='arquivos')
    pdf = models.FileField(upload_to='pdfs/')

