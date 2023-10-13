from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Tyans(models.Model):
    name = models.CharField('Имя', max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")  # поле слага
    age = models.IntegerField('Возраст', null=True)
    face = models.FloatField('Лицо')
    figure = models.FloatField('Фигура')
    tits = models.FloatField('Тема сисек')
    ass = models.FloatField('Жопа')
    image = models.URLField('Фото', max_length=200)
    date = models.DateTimeField('Дата и время публикации', auto_now_add=True)
    time_update = models.DateTimeField('Время изменения', auto_now=True)
    is_published = models.BooleanField('Публикация', default=True)
    cat = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, blank=True)
    user = models.ForeignKey('TopUser', null=True, blank=True, on_delete=models.PROTECT)

    @property
    def rating(self):
        average = round((self.face + self.figure + self.tits + self.ass) / 4, 2)
        return average

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Тянка'
        verbose_name_plural = 'Тянки'
        # ordering = ['date', 'name']


class Category(models.Model):
    name = models.CharField('Категория', max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")  # поле слага

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class TopUser(AbstractUser):
    profile_image = models.URLField('Фото', max_length=200, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('user_scores', args=[str(self.username)])
