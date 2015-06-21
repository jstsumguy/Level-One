# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0028_auto_20150507_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge_score',
            name='solution',
            field=models.FileField(null=True, upload_to=b'competitive_solutions/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 8, 1, 46, 34, 70962), null=True),
        ),
    ]
