# Generated by Django 2.1.1 on 2018-10-19 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181018_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seccion',
            name='profesor',
        ),
        migrations.RemoveField(
            model_name='etiqueta',
            name='asesoria',
        ),
        migrations.DeleteModel(
            name='Seccion',
        ),
    ]