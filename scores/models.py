from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


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


class Article(models.Model):
    name = models.CharField('Имя', max_length=200)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")  # поле слага
    age = models.IntegerField('Возраст', null=True)
    ratings = models.ManyToManyField(get_user_model(), through='ArticleRating')
    total_rating = models.DecimalField('Рейтинг', max_digits=5, decimal_places=2, default=0.0, blank=True)
    user_count = models.IntegerField('Кол-во оценок', null=True, blank=True)
    photo = models.URLField('Фото', max_length=200, blank=True, null=True)
    created_at = models.DateTimeField('Дата и время публикации', auto_now_add=True)
    time_update = models.DateTimeField('Время изменения', auto_now=True)
    is_published = models.BooleanField('Публикация', default=True)
    cat = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Дама'
        verbose_name_plural = 'Дамы'


class ArticleRating(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='ratings')
    article = models.ForeignKey("Article", on_delete=models.PROTECT)
    face = models.DecimalField('Лицо', max_digits=5, decimal_places=2, default=0.0)
    figure = models.DecimalField('Фигура', max_digits=5, decimal_places=2, default=0.0)
    tits = models.DecimalField('Тема сисек', max_digits=5, decimal_places=2, default=0.0)
    ass = models.DecimalField('Жопа', max_digits=5, decimal_places=2, default=0.0)

    @property
    def avg_rating(self):
        return (self.face + self.figure + self.tits + self.ass) / 4

    def __str__(self):
        return f"{self.user} - {self.article}"

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'


