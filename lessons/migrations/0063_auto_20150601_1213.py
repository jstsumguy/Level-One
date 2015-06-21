# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0062_auto_20150601_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='quiz_score',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 12, 13, 23, 463139), auto_now=True),
        ),
    ]
