from django import forms
from .models import JobOffer

class JobOfferForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = ['title', 'description', 'requirements', 'contract_type', 'location', 'salary']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Desarrollador Backend Django'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe las responsabilidades del puesto...'
            }),
            'requirements': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4,
                'placeholder': 'Lista los requisitos y habilidades necesarias...'
            }),
            'contract_type': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Bogotá, Colombia'
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 4000000'
            }),
        }
        labels = {
            'title': 'Título del Puesto',
            'description': 'Descripción',
            'requirements': 'Requisitos',
            'contract_type': 'Tipo de Contrato', 
            'location': 'Ubicación',
            'salary': 'Salario (OPCIONAL)',
        }