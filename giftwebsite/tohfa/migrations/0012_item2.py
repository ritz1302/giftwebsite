# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0011_subscribe_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item2',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='Date Published')),
                ('image1', models.ImageField(upload_to='', blank=True)),
                ('image2', models.ImageField(upload_to='', blank=True)),
                ('image3', models.ImageField(upload_to='', blank=True)),
                ('image4', models.ImageField(upload_to='', blank=True)),
                ('image5', models.ImageField(upload_to='', blank=True)),
                ('image6', models.ImageField(upload_to='', blank=True)),
                ('price', models.FloatField()),
                ('old_price', models.FloatField()),
                ('description', models.CharField(max_length=500)),
                ('discount', models.IntegerField(blank=True)),
                ('catagory', models.CharField(max_length=200)),
                ('sub_catagory', models.CharField(max_length=200)),
                ('sub_sub_catagory', models.CharField(max_length=200)),
                ('item_number', models.IntegerField()),
                ('product_id', models.IntegerField()),
            ],
        ),
    ]
