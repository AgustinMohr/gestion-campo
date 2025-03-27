from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Usuario

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegistroForm(UserCreationForm):
    nombre_completo = forms.CharField(label="Nombre Completo", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = ["username", "nombre_completo", "password1", "password2"]
