# Generated by Django 2.0.2 on 2018-02-09 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocatorias', '0003_auto_20180207_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convocatoria',
            name='contacto',
            field=models.CharField(max_length=128, verbose_name='Contacto'),
        ),
    ]
