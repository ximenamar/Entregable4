# Generated by Django 2.1.1 on 2018-10-19 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_alumno', models.CharField(default='Alumno', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Asesoria_multiple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_asesoria_multiple', models.CharField(default='AseMul', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Asesoria_simple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_asesoria_simple', models.CharField(default='AseSim', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_cita', models.CharField(default='Cita', max_length=200)),
                ('fecha', models.CharField(max_length=200)),
                ('razon', models.CharField(max_length=200)),
                ('lugar', models.CharField(max_length=200)),
                ('asesoria_multiple', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Asesoria_multiple')),
                ('asesoria_simple', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Asesoria_simple')),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_etiqueta', models.CharField(default='Etiqueta', max_length=200)),
                ('asesoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Asesoria_simple')),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_facultad', models.CharField(default='Facultad', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_horario', models.CharField(default='horario', max_length=200)),
                ('inicio', models.CharField(max_length=200)),
                ('fin', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_seccion', models.CharField(default='Seccion', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_semestre', models.CharField(default='Semestre', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='curso',
            name='carrera',
        ),
        migrations.AlterField(
            model_name='carrera',
            name='nombre_carrera',
            field=models.CharField(default='Carrera', max_length=200),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nombre_curso',
            field=models.CharField(default='Curso', max_length=200),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='nombre_profesor',
            field=models.CharField(default='Profesor', max_length=200),
        ),
        migrations.AddField(
            model_name='seccion',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Profesor'),
        ),
        migrations.AddField(
            model_name='horario',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Profesor'),
        ),
        migrations.AddField(
            model_name='facultad',
            name='carrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Carrera'),
        ),
        migrations.AddField(
            model_name='facultad',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Seccion'),
        ),
        migrations.AddField(
            model_name='etiqueta',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Profesor'),
        ),
        migrations.AddField(
            model_name='curso',
            name='facultad',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.Facultad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='seccion',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.Seccion'),
            preserve_default=False,
        ),
    ]
