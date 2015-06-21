# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0060_quiz_score_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
        migrations.RemoveField(
            model_name='course',
            name='length',
        ),
        migrations.AlterField(
            model_name='quiz_score',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 12, 0, 17, 195702), auto_now=True),
        ),
    ]
