# Generated by Django 3.1.4 on 2020-12-19 15:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_auto_20201216_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 19, 15, 54, 38, 448059, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 19, 15, 54, 38, 448059, tzinfo=utc)),
        ),
    ]