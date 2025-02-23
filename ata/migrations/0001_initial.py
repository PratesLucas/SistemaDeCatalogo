# Generated by Django 5.0.4 on 2024-08-30 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('serie', models.CharField(max_length=50)),
                ('turma', models.CharField(max_length=50)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='atas/')),
            ],
        ),
        migrations.CreateModel(
            name='ArquivoPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='pdfs/')),
                ('nome', models.CharField(blank=True, max_length=255)),
                ('ata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ata.atas')),
            ],
        ),
    ]
