# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tohfa', '0012_item2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Catagory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=200)),
                ('catagory', models.ForeignKey(to='tohfa.Catagory')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Sub_Catagory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('sub_sub_name', models.CharField(max_length=200)),
                ('catagory', models.ForeignKey(to='tohfa.Catagory')),
                ('sub_catagory', models.ForeignKey(to='tohfa.Sub_Catagory')),
            ],
        ),
    ]
