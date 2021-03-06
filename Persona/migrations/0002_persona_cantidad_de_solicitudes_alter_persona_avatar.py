# Generated by Django 4.0 on 2021-12-20 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Persona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='cantidad_de_solicitudes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='persona',
            name='avatar',
            field=models.ImageField(upload_to='Persona/Y%/m%/d%/'),
        ),
    ]
