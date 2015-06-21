# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0063_auto_20150601_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='created',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quiz_score',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 13, 36, 8, 526657), auto_now=True),
        ),
    ]
