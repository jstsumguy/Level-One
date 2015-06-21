# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0061_auto_20150601_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.ForeignKey(to='lessons.Student', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quiz_score',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 12, 9, 51, 579388), auto_now=True),
        ),
    ]
