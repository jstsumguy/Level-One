# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0067_auto_20150603_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=models.TextField(default=b"You haven't added any content yet"),
        ),
        migrations.AlterField(
            model_name='quiz_score',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 13, 42, 52, 107958), auto_now=True),
        ),
    ]
