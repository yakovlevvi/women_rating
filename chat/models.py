from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Messages(models.Model):
    author = models.ForeignKey(User, models.CASCADE, verbose_name='Автор')
    text = models.CharField('Текст сообщения', max_length=200)
    created_at = models.DateTimeField('Дата и время отправки', auto_now_add=True)

    def __str__(self):
        return f'{self.author} : {self.text}'

    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщение'
