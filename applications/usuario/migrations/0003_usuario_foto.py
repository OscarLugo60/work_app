# Generated by Django 4.2.4 on 2023-08-15 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuario_groups_usuario_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='medicos'),
        ),
    ]
