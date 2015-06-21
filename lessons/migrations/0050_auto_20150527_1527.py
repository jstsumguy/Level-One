# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0049_auto_20150527_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='points',
        ),
        migrations.AlterField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 15, 27, 53, 471921), auto_now=True),
        ),
    ]
