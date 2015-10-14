# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0005_item_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('auther', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='Date Published')),
                ('comments', models.IntegerField()),
                ('hits', models.IntegerField()),
                ('description', models.CharField(max_length=20000)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
