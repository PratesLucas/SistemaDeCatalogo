from .models import Pessoa
from django import forms
from django.forms import ModelForm, TextInput

class PessoaForm(ModelForm):

    class Meta():
        model = Pessoa
        fields = ['nome', 'cpf', 'idade', 'rg']
        widgets = {
                'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
                'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu CPF'}),
                'idade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua idade'}), 
                'rg': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu RG'}),
        }

class LoginForm(forms.Form):
    usuario = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu usuário'})
    )
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )