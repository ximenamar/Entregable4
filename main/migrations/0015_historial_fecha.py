# Generated by Django 2.1.1 on 2018-11-12 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_historial_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default='2018-11-12', verbose_name='fecha atendido'),
            preserve_default=False,
        ),
    ]