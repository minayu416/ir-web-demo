# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='emailaddress',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
