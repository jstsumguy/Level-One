# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0033_auto_20150511_0208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson_Question_Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('likes', models.IntegerField(default=0)),
                ('answer', models.TextField()),
                ('question', models.ForeignKey(to='lessons.Lesson_Question')),
                ('student', models.ForeignKey(to='lessons.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='lesson_question',
            name='answer',
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 12, 16, 23, 221410), null=True),
        ),
    ]
