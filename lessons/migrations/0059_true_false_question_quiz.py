# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0058_true_false_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='true_false_question',
            name='quiz',
            field=models.ForeignKey(to='lessons.Quiz', null=True),
            preserve_default=True,
        ),
    ]
