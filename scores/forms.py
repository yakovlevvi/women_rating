from django import forms
from .models import Tyans, Category
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user


class TyanForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select, empty_label="Категория не выбрана")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Tyans
        fields = ['name', 'slug', 'age', 'face', 'figure', 'tits', 'ass', 'image', 'cat']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сюда вводить имя латиницей (name-example)',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст',
            }),
            'face': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Лицо',
            }),
            'figure': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фигура',
            }),
            'tits': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема сисек',
            }),
            'ass': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Жопа',
            }),
            'image': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на фото',
            }),
        }

    def clean_title(self):
        title = self.cleaned_data['name']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title
