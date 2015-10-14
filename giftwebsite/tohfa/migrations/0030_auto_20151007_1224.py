# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0029_auto_20151002_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item3',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
                ('item_number', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('catagory', models.ForeignKey(to='tohfa.Catagory')),
                ('sub_catagory', smart_selects.db_fields.ChainedForeignKey(chained_field='catagory', auto_choose=True, to='tohfa.Sub_Catagory', chained_model_field='catagory')),
            ],
        ),
        migrations.RemoveField(
            model_name='item2',
            name='sub_sub_catagory',
        ),
        migrations.AddField(
            model_name='item2',
            name='catagory',
            field=models.ForeignKey(to='tohfa.Catagory', default=1),
            preserve_default=False,
        ),
    ]
