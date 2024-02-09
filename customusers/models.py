from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    profile_image = models.URLField('Фото', max_length=200, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('user_scores', args=[str(self.username)])