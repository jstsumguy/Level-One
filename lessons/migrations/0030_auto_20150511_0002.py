# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0029_auto_20150508_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge_score',
            name='comments',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 0, 2, 49, 805699), null=True),
        ),
    ]
