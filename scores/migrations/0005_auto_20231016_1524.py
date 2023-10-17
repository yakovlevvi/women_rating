# Generated by Django 3.1 on 2023-10-16 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0004_auto_20231016_1148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlerating',
            options={'verbose_name': 'Оценка', 'verbose_name_plural': 'Оценки'},
        ),
        migrations.AlterField(
            model_name='articlerating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ratings', to=settings.AUTH_USER_MODEL),
        ),
    ]
