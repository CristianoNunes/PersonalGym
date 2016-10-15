# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalGym', '0003_auto_20161014_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(max_length=9),
        ),
    ]
