# Generated by Django 3.1.4 on 2020-12-06 17:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0002_auto_20201206_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='joined_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 6, 17, 31, 57, 772112, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to=settings.AUTH_USER_MODEL),
        ),
    ]
