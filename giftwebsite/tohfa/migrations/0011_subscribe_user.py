# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0010_blog_filter_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe_user',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('mail', models.CharField(max_length=200)),
            ],
        ),
    ]
