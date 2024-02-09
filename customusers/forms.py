from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from .models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    profile_image = forms.CharField(label='Фото профиля', widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ссылка на фото (скопировать URL из браузера)'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '********'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '********'}))

    class Meta:
        model = User
        fields = {'username', 'profile_image', 'password1', 'password2'}


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = {'username', 'profile_image'}


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']