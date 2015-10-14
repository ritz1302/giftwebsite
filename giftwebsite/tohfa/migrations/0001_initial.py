# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='Date Published')),
                ('image1', models.ImageField(upload_to='', blank=True)),
                ('image2', models.ImageField(upload_to='', blank=True)),
                ('image3', models.ImageField(upload_to='', blank=True)),
                ('image4', models.ImageField(upload_to='', blank=True)),
                ('image5', models.ImageField(upload_to='', blank=True)),
                ('image6', models.ImageField(upload_to='', blank=True)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=500)),
                ('discount', models.IntegerField(blank=True)),
                ('brand', models.CharField(max_length=200)),
                ('catagory', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
            ],
        ),
    ]
