import random
import requests
from faker import Faker
from django.core.management.base import BaseCommand
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from ata.models import Atas  # Certifique-se de ajustar para o nome real do seu app

fake = Faker('pt_BR')

def baixar_pdf_fake():
    url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
    r = requests.get(url)
    if r.status_code == 200:
        temp_file = NamedTemporaryFile()
        temp_file.write(r.content)
        temp_file.flush()
        return temp_file
    return None

def criar_dados_falsos(n=10):
    for _ in range(n):
        ano = fake.year()
        serie = fake.word().capitalize()
        turma = fake.word().capitalize()

        temp_pdf = baixar_pdf_fake()
        if temp_pdf:
            ata = Atas(
                ano=ano,
                serie=serie,
                turma=turma,
            )
            ata.pdf.save(f"{serie}_{turma}_{ano}.pdf", File(temp_pdf))
            ata.save()
            print(f"Ata {ata} criada com sucesso!")
        else:
            print("Falha ao baixar PDF. Ata não foi criada.")

class Command(BaseCommand):
    help = 'Preenche o banco de dados com dados falsos no modelo Atas'

    def add_arguments(self, parser):
        parser.add_argument(
            '--quantidade',
            type=int,
            default=10,
            help='Número de atas a serem criadas',
        )

    def handle(self, *args, **kwargs):
        quantidade = kwargs['quantidade']
        criar_dados_falsos(quantidade)
        self.stdout.write(self.style.SUCCESS(f'{quantidade} atas criadas com sucesso!'))
