# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0009_auto_20150924_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='filter_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
