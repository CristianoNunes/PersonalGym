# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalGym', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treino',
            name='aluno',
            field=models.ForeignKey(to='PersonalGym.Aluno', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treino',
            name='exercicio',
            field=models.ForeignKey(to='PersonalGym.Exercicio', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treino',
            name='serie',
            field=models.ForeignKey(to='PersonalGym.Serie', default=0),
            preserve_default=False,
        ),
    ]
