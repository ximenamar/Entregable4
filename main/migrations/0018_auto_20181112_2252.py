# Generated by Django 2.1.1 on 2018-11-13 03:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20181112_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]
