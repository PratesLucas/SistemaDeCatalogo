from .models import Pessoa
from django import forms
from django.forms import ModelForm, TextInput

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'cpf', 'pdf']
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome'}),
            'cpf': TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CPF (apenas números)'}),
        }

class LoginForm(forms.Form):
    usuario = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu usuário'})
    )
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )