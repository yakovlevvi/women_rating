from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from scores.models import *


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Логин'}))
    profile_image = forms.CharField(label='Фото профиля', widget=forms.URLInput(attrs={'class': 'form-input', 'placeholder': 'Ссылка на фото'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': '********'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': '********'}))

    class Meta:
        model = TopUser
        fields = ('username', 'profile_image', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = TopUser
        fields = {'username', 'profile_image'}


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': '********'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))