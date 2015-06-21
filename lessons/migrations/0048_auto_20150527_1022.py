# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0047_auto_20150527_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson_question',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='lesson_question_answer',
            name='likes',
        ),
        migrations.AddField(
            model_name='lesson_answer_like',
            name='answer',
            field=models.ForeignKey(to='lessons.Lesson_Question_Answer', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson_question_like',
            name='question',
            field=models.ForeignKey(to='lessons.Lesson_Question', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 10, 22, 47, 358231), auto_now=True),
        ),
    ]
