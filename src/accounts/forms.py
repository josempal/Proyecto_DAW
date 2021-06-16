# Django
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
# App
from .models import User

class LoginForm(AuthenticationForm):

    username = forms.CharField(
        label='Nombre de usuario', widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Nombre de usuario',
                'id': 'username'
            }   
    ))

    password_confirm = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'id': 'password'
            }   
    ))

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Obligatorio. El email debe existir')

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'email', 'password1', 'password2', )
"""
class SignupForm(forms.Form):

    username = forms.CharField(
        label='Nombre de usuario', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required': 'Ingrese un email por favor'})
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        validate = User.objects.filter(username=username)
        if validate.count():
            raise ValidationError("Nombre de usuario en uso")
        return self.cleaned_data['username']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Email en uso')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Nombre de usuario'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repite la contraseña'})
"""