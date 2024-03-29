# Generated by Django 2.2.3 on 2019-07-27 10:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='closed_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата-время закрытия'),
        ),
        migrations.AlterField(
            model_name='record',
            name='rate',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка'),
        ),
    ]
