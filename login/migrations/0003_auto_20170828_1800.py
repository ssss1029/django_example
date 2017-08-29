# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_favorited_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='favorited_books',
            field=models.ManyToManyField(blank=True, null=True, to='user_page.Book'),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
