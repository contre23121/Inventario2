from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario',
        max_length=50,
        error_messages={'required': 'El nombre de usuario es obligatorio.'}
    )
    password = forms.CharField(
        label='Contraseña',
        max_length=12,
        widget=forms.PasswordInput,
        error_messages={'required': 'La contraseña es obligatoria.'}
    )
