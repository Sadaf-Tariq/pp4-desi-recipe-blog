# Generated by Django 3.2 on 2023-11-03 13:15

import django.core.validators
from django.db import migrations, models
import recipeblog.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.FloatField(default=0, validators=[recipeblog.models.field_validation, django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
