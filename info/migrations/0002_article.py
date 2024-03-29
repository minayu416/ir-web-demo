# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Artid', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=32, blank=True)),
                ('content', models.TextField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
