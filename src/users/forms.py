# Django
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# 3rd party
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
'''class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)'''

""" class SignupForm(forms.Form):

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )
    username = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.TextInput()
    )
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )


    def clean(self):

        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return data

    def save(self):
      
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

 """
class SignupForm(PopRequestMixin, CreateUpdateAjaxMixin,
                UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']