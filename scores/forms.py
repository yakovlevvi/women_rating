from django import forms
from django.forms import widgets
from django.utils.text import slugify

from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user
from unidecode import unidecode


class TyanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Article
        fields = ['name', 'age', 'photo', 'cat']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст',
            }),
            'photo': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на фото',
            }),
            'cat': forms.Select(attrs={
                'class': 'form-control'
            })
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        name = self.cleaned_data.get('name')
        if name:
            slug = slugify(unidecode(name))
            instance.slug = slug
        if commit:
            instance.save()
        return instance

    def clean_title(self):
        title = self.cleaned_data['name']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title


class ArticleRatingForm(forms.ModelForm):
    face = forms.DecimalField(min_value=0, max_value=10, decimal_places=1, max_digits=5, required=True,
                              label='Лицо', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    figure = forms.DecimalField(min_value=0, max_value=10, decimal_places=1, max_digits=5, required=True,
                                label='Фигура', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    tits = forms.DecimalField(min_value=0, max_value=10, decimal_places=1, max_digits=5, required=True,
                              label='Тема сисек', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ass = forms.DecimalField(min_value=0, max_value=10, decimal_places=1, max_digits=5, required=True,
                             label='Жопа', widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ArticleRating
        fields = ['face', 'figure', 'tits', 'ass']

