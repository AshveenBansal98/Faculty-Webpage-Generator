# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0018_about_us_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='img',
            field=models.CharField(default='https://upload.wikimedia.org/wikipedia/en/thumb/1/12/IIT_Guwahati_Logo.svg/760px-IIT_Guwahati_Logo.svg.png', max_length=400),
            preserve_default=False,
        ),
    ]
