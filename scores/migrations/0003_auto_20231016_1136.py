# Generated by Django 3.1 on 2023-10-16 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0002_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='rating_count',
        ),
        migrations.RemoveField(
            model_name='article',
            name='total_rating',
        ),
        migrations.RemoveField(
            model_name='article',
            name='user',
        ),
        migrations.CreateModel(
            name='ArticleRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Лицо')),
                ('figure', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Фигура')),
                ('tits', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Тема сисек')),
                ('ass', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Тема сисек')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scores.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='ratings',
            field=models.ManyToManyField(through='scores.ArticleRating', to=settings.AUTH_USER_MODEL),
        ),
    ]
