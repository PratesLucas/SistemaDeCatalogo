from .models import Atas, ArquivoPDF
from django import forms
from django.forms import ModelForm, TextInput


class AtasForm(ModelForm):

    class Meta():
        model = Atas
        fields = ['ano', 'serie', 'turma']
        widgets = {
            'ano': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ano'}),
            'serie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Série'}),
            'turma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Turma'}),
        }
        labels = {
            'ano': 'Ano:',
            'serie': 'Série:',
            'turma': 'Turma:',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
            'class': 'form-input block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 mb-4'
        })


class ArquivoPDFForm(forms.ModelForm):
    class Meta:
        model = ArquivoPDF
        fields = ['pdf', 'nome']
        widgets = {
            'pdf': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'PDF'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        }
        labels = {
            'pdf': 'PDF:',
            'nome': 'Nome:',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
            'class': 'form-input block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 mb-4'
        })
