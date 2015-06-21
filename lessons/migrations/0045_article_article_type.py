# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0044_remove_challenge_score_solution'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
