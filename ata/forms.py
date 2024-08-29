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

class ArquivoPDFForm(forms.ModelForm):
    class Meta:
        model = ArquivoPDF
        fields = ['pdf', 'nome']