# Generated by Django 2.1.1 on 2018-11-01 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_asesoria_asesoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_administrador', models.CharField(default='Profesor', max_length=200)),
            ],
        ),
    ]
