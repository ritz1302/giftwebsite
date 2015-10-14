# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0003_item_old_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='link',
            field=models.CharField(default='abc', max_length=500),
            preserve_default=False,
        ),
    ]
