# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0008_blog_filter_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='filter_id',
            field=models.CharField(max_length=100),
        ),
    ]
