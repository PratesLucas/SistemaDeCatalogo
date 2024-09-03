from django.core.exceptions import ValidationError
from .models import Usuario
from django import forms
from django.contrib.auth.hashers import make_password


class UsuarioForm(forms.ModelForm):
    password2 = forms.CharField(
        label='Confirmação de senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control dark:bg-gray-700 dark:border-gray-600 dark:text-gray-300', 'placeholder': 'Confirme sua senha'}),
        required=True
    )
    
    tipo_user = forms.ChoiceField(
        label='Tipo de Usuário',
        choices=Usuario.TIPO_CHOICES,
    )
    
    class Meta:
        model = Usuario
        fields = ['username', 'cpf', 'email', 'tipo_user', 'password']
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control dark:bg-gray-700 dark:border-gray-600 dark:text-gray-300', 'placeholder': 'Digite seu usuário'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control dark:bg-gray-700 dark:border-gray-600 dark:text-gray-300', 'placeholder': 'Digite seu CPF'}),
            'email': forms.EmailInput(attrs={'class': 'form-control dark:bg-gray-700 dark:border-gray-600 dark:text-gray-300', 'placeholder': 'Digite seu email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control dark:bg-gray-700 dark:border-gray-600 dark:text-gray-300', 'placeholder': 'Digite sua senha'}),
            'tipo_user': forms.Select(attrs={'class': 'form-control dark:bg-gray-700 dark:border-gray-600 dark:text-gray-300'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = self.instance

        if user.__class__.objects.filter(username=username).exclude(pk=user.pk).exists():
            raise ValidationError("Já existe um usuário com esse nome.")

        return username
    
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        
        if password and password2 and password != password2:
            self.add_error('password2', 'As senhas não coincidem.')
        
        cleaned_data["password"] = make_password(password)
        
        return cleaned_data
