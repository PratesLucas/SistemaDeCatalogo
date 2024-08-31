import random
import requests
from faker import Faker
from django.core.management.base import BaseCommand
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from pessoa.models import Pessoa  # Certifique-se de ajustar para o nome real do seu app

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

def gerar_cpf_unico():
    while True:
        cpf = fake.unique.cpf().replace('.', '').replace('-', '')
        if not Pessoa.objects.filter(cpf=cpf).exists():
            return cpf

def criar_dados_falsos_pessoas(n=10):
    for _ in range(n):
        cpf = gerar_cpf_unico()
        temp_pdf = baixar_pdf_fake()
        if temp_pdf:
            pessoa = Pessoa(
                nome=fake.name(),
                cpf=cpf,
            )
            pessoa.pdf.save(f"{cpf}.pdf", File(temp_pdf))
            pessoa.save()
            print(f"Pessoa {pessoa.nome} criada com sucesso!")
        else:
            print("Falha ao baixar PDF. Pessoa não foi criada.")

class Command(BaseCommand):
    help = 'Preenche o banco de dados com dados falsos no modelo Pessoa'

    def add_arguments(self, parser):
        parser.add_argument(
            '--quantidade',
            type=int,
            default=10,
            help='Número de pessoas a serem criadas',
        )

    def handle(self, *args, **kwargs):
        quantidade = kwargs['quantidade']
        criar_dados_falsos_pessoas(quantidade)
        self.stdout.write(self.style.SUCCESS(f'{quantidade} pessoas criadas com sucesso!'))
