from django.db import models

class Atas(models.Model):
    ano = models.IntegerField()
    serie = models.CharField(max_length=50)
    turma = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='atas/', null=True, blank=True)

    def __str__(self):
        return f"Ata {self.ano} - {self.serie} - {self.turma}"