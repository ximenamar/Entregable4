# Generated by Django 2.1.1 on 2018-11-19 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_asesoria_multiple_mensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='asesoria_multiple',
            name='esatado3',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
