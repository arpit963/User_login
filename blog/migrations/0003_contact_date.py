# Generated by Django 2.2.17 on 2021-01-28 11:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 1, 28, 11, 37, 37, 204492)),
        ),
    ]