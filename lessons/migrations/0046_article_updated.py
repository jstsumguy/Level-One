# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0045_article_article_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 21, 55, 10, 339566), auto_now=True),
            preserve_default=True,
        ),
    ]
