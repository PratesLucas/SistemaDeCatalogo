from django.db import models


class Atas(models.Model):
    SERIES = [('1', '1º ano'), ('2', '2º ano'), ('3', '3º ano'), ('4', '4º ano'), ('5', '5º ano'), ('6', '6º ano')]
    TURMAS = [('A', 'Turma A'), ('B', 'Turma B'), ('C', 'Turma C'), ('D', 'Turma D'), ('E', 'Turma E'), ('F', 'Turma F')]
    
    ano = models.IntegerField()
    serie = models.CharField(max_length=50, choices=SERIES)
    turma = models.CharField(max_length=50, choices=TURMAS)
    pdf = models.FileField(upload_to='atas/', null=True, blank=True)

    def __str__(self):
        return f"Ata {self.ano} - {self.serie} - {self.turma}"


class ArquivoPDF(models.Model):
    ata = models.ForeignKey(Atas, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='pdfs/')
    nome = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nome if self.nome else f'PDF {self.id}'
