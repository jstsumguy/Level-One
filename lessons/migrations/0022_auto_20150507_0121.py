# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0021_auto_20150507_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson_question',
            name='answer',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 1, 21, 17, 368813), null=True),
        ),
    ]
