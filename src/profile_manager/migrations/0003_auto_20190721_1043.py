# Generated by Django 2.0.13 on 2019-07-21 17:43

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('profile_manager', '0002_profile_silent_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hidden_quests',
            field=models.CharField(blank=True, max_length=1023, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
