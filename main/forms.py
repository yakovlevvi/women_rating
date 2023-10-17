from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from scores.models import *


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    profile_image = forms.CharField(label='Фото профиля', widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ссылка на фото (скопировать URL из браузера)'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '********'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '********'}))

    class Meta:
        model = TopUser
        fields = {'username', 'profile_image', 'password1', 'password2'}


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = TopUser
        fields = {'username', 'profile_image'}


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '********'}))




class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255, widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }))
    content = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'cols': 60, 'rows': 10,
        'placeholder': 'Сообщение'}))