# Generated by Django 2.1.1 on 2018-11-19 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_asesoria_multiple_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='asesoria_multiple',
            name='estado2',
            field=models.CharField(max_length=200, null=True),
        ),
    ]