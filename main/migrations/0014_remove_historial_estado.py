# Generated by Django 2.1.1 on 2018-11-12 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_historial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historial',
            name='estado',
        ),
    ]
