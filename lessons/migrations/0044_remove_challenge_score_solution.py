# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0043_course_lesson_activity_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge_score',
            name='solution',
        ),
    ]
