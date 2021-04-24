from django import forms
from .models import register


class Employee(forms.ModelForm):
    class Meta:
        model = register
        fields = ['First_name', 'Last_name', 'Email', 'Password']
        widgets = {
            'First_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control'}),

        }
