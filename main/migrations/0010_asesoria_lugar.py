# Generated by Django 2.1.1 on 2018-10-30 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_cita_simple_razon'),
    ]

    operations = [
        migrations.AddField(
            model_name='asesoria',
            name='lugar',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
