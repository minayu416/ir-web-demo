# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160824_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='intro',
            field=models.TextField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pages',
            name='menu',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
