# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0016_auto_20150930_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item3',
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
                ('item_number', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('catagory', models.ForeignKey(to='tohfa.Catagory')),
                ('sub_catagory', smart_selects.db_fields.ChainedForeignKey(chained_field='catagory', to='tohfa.Sub_Catagory', chained_model_field='catagory', auto_choose=True)),
                ('sub_sub_catagory', smart_selects.db_fields.ChainedForeignKey(chained_field='sub_catagory', to='tohfa.Sub_Sub_Catagory', chained_model_field='sub_catagory', auto_choose=True)),
            ],
        ),
    ]
