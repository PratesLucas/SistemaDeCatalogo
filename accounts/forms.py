from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class UsuarioForm(UserCreationForm):
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )
    password2 = forms.CharField(
        label='Confirmação de senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'})
    )

    
    class Meta():
        model = Usuario
        fields = ['nome', 'username', 'cpf', 'email']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu usuário'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu CPF'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email'}),
        }
