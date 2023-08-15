# Generated by Django 4.2.4 on 2023-08-15 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='Nombre de Usuario')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('nivel', models.CharField(blank=True, choices=[('0', 'Administrador'), ('1', 'Coordinador')], max_length=1)),
                ('is_staff', models.BooleanField(default=False)),
                ('estatus', models.CharField(choices=[('0', 'Activo'), ('1', 'Anulado')], max_length=1, verbose_name='Estatus')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.departamento')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
