# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0059_true_false_question_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz_score',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 29, 21, 16, 10, 342277), auto_now=True),
            preserve_default=True,
        ),
    ]
