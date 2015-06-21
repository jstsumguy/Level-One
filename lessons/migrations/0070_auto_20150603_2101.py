# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0069_auto_20150603_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson_project',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='quiz_score',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 21, 1, 38, 120099), auto_now=True),
        ),
    ]
