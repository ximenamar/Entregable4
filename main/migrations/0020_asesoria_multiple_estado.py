# Generated by Django 2.1.1 on 2018-11-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20181118_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='asesoria_multiple',
            name='estado',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
