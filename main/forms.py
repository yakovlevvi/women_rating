from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255, widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }))
    content = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'cols': 60, 'rows': 10,
        'placeholder': 'Сообщение'}))