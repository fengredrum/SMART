# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-12-10 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0053_irrlog_label_reason"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datalabel",
            name="label_reason",
            field=models.TextField(default="", null=True),
        ),
        migrations.AlterField(
            model_name="irrlog",
            name="label_reason",
            field=models.TextField(default="", null=True),
        ),
    ]
