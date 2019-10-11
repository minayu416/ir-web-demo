# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20170515_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='irdb_cata',
            field=models.CharField(default=b'\xe7\x84\xa1', max_length=32, choices=[(b'', b'\xe7\x84\xa1'), (b'enter', b'\xe5\x85\xa5\xe5\xad\xb8\xe7\xab\xaf'), (b'inschool', b'\xe5\x9c\xa8\xe5\xad\xb8\xe7\xab\xaf'), (b'graduate', b'\xe7\x95\xa2\xe6\xa5\xad\xe7\xab\xaf')]),
            preserve_default=True,
        ),
    ]
