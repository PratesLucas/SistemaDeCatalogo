from django import forms
import django_filters
from .models import Atas

class AtasFilter(django_filters.FilterSet):
    ano = django_filters.NumberFilter(
        field_name='ano', 
        lookup_expr='exact', 
        label='Ano', 
        widget=forms.NumberInput(
            attrs={
                'class': 'shadow-md w-full pl-2 pr-2 text-sm text-gray-700 placeholder-gray-600 bg-gray-100 border-0 rounded-md dark:placeholder-gray-500 dark:focus:shadow-outline-gray dark:focus:placeholder-gray-600 dark:bg-gray-700 dark:text-gray-200 focus:placeholder-gray-500 focus:bg-white focus:border-purple-300 focus:outline-none focus:shadow-outline-purple form-input', 'placeholder': 'Ano'
            }
        ),
    )
    
    serie = django_filters.ChoiceFilter(
        field_name='serie', 
        lookup_expr='icontains', 
        label='Série',
        choices=Atas.SERIES,
        empty_label="Selecione a série",
        widget=forms.Select(
            attrs={
                'class': 'shadow-md w-full pl-2 pr-2 text-sm text-gray-700 placeholder-gray-600 bg-gray-100 border-0 rounded-md dark:placeholder-gray-500 dark:focus:shadow-outline-gray dark:focus:placeholder-gray-600 dark:bg-gray-700 dark:text-gray-200 focus:placeholder-gray-500 focus:bg-white focus:border-purple-300 focus:outline-none focus:shadow-outline-purple form-input', 'placeholder': 'Ano'
            }
        ),
    )
    
    turma = django_filters.ChoiceFilter(
        field_name='turma', 
        choices=Atas.TURMAS,
        lookup_expr='icontains',
        empty_label="Selecione a turma",
        label='Turma', 
        widget=forms.Select(
            attrs={
                'class': 'shadow-md w-full pl-2 pr-2 text-sm text-gray-700 placeholder-gray-600 bg-gray-100 border-0 rounded-md dark:placeholder-gray-500 dark:focus:shadow-outline-gray dark:focus:placeholder-gray-600 dark:bg-gray-700 dark:text-gray-200 focus:placeholder-gray-500 focus:bg-white focus:border-purple-300 focus:outline-none focus:shadow-outline-purple form-input', 'placeholder': 'Ano'
            }
        ),
    )

    class Meta:
        model = Atas
        fields = ['ano', 'serie', 'turma']
