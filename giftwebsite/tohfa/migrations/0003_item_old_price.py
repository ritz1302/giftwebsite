# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0002_item_item_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='old_price',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
    ]
