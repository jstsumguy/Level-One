# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0034_auto_20150518_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz_question',
            name='quiz',
        ),
        migrations.DeleteModel(
            name='Quiz_Question',
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 16, 58, 49, 640366), null=True),
        ),
    ]
