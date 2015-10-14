# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0019_item3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
                ('sub_catagory', smart_selects.db_fields.ChainedForeignKey(to='tohfa.Sub_Catagory', auto_choose=True, chained_model_field='catagory', chained_field='catagory')),
                ('sub_sub_catagory', smart_selects.db_fields.ChainedForeignKey(to='tohfa.Sub_Sub_Catagory', auto_choose=True, chained_model_field='sub_catagory', chained_field='sub_catagory')),
            ],
        ),
        migrations.RemoveField(
            model_name='item3',
            name='catagory',
        ),
        migrations.RemoveField(
            model_name='item3',
            name='sub_catagory',
        ),
        migrations.DeleteModel(
            name='Item3',
        ),
    ]
