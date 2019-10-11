# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_register_emailaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='validate',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
