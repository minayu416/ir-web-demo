# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20191014_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='photo',
            field=models.CharField(default=b'static/img/article_img/default.png', max_length=255),
            preserve_default=True,
        ),
    ]
