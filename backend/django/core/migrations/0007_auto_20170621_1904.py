# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 19:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_assigneddata_assigned_timestamp"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="assigneddata", unique_together=set([("user", "queue")]),
        ),
    ]
