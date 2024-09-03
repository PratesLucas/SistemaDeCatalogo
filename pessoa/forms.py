from .models import Pessoa
from django import forms
from django.forms import ModelForm


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'cpf', 'pdf', 'tipo_pessoa']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-input block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 mb-4',
                'placeholder': 'Digite o nome'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-input block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 mb-4',
                'placeholder': 'Digite o CPF (apenas números)'
            }),
            'pdf': forms.ClearableFileInput(attrs={
                'class': 'form-input block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 mb-4'
            }),
            'tipo_pessoa': forms.Select(attrs={
                'class': 'form-input block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 mb-4'
            }),
        }
        labels = {
            'nome': 'Nome:',
            'cpf': 'CPF:',
            'pdf': 'PDF:',
            'tipo_pessoa': 'Tipo de pessoa:',
        }
        help_texts = {
            'pdf': 'Envie um arquivo PDF.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-input block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 mb-4'
            })


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuário", widget=forms.TextInput(attrs={
        'class': 'form-input', 
        'placeholder': 'Usuário'
    }))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={
        'class': 'form-input', 
        'placeholder': 'Senha'
    }))
    

from django import forms
from .models import Endereco

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'bairro', 'num', 'complemento', 'cidade', 'cep', 'estado']
        widgets = {
            'rua': forms.TextInput(attrs={
                'class': 'form-input block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 mb-4',
                'placeholder': 'Digite o nome da rua'
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-input block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 mb-4',
                'placeholder': 'Digite o bairro'
            }),
            'num': forms.NumberInput(attrs={
                'class': 'form-input block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 mb-4',
                'placeholder': 'Número'
            }),
            'complemento': forms.TextInput(attrs={
                'class': 'form-input block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 mb-4',
                'placeholder': 'Complemento'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-input block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 mb-4',
                'placeholder': 'Cidade'
            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-input block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 mb-4',
                'placeholder': 'CEP'
            }),
            'estado': forms.TextInput(attrs={
                'class': 'form-input block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 mb-4',
                'placeholder': 'Estado (UF)'
            }),
        }
        labels = {
            'rua': 'Rua:',
            'bairro': 'Bairro:',
            'num': 'Número:',
            'complemento': 'Complemento:',
            'cidade': 'Cidade:',
            'cep': 'CEP:',
            'estado': 'Estado:',
        }