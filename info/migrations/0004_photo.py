# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photoid', models.CharField(max_length=32)),
                ('description', models.TextField(max_length=255, blank=True)),
                ('photo', models.FileField(upload_to=b'static/img/IRinfo/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
