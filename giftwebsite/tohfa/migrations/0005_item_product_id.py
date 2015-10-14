# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0004_item_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='product_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
