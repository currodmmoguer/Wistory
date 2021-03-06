# Generated by Django 3.1.7 on 2021-02-28 12:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20210228_1227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargo',
            options={'verbose_name': 'Cargo', 'verbose_name_plural': 'Cargos'},
        ),
        migrations.AlterModelOptions(
            name='dinastia',
            options={'verbose_name': 'Dinastía', 'verbose_name_plural': 'Dinastías'},
        ),
        migrations.AlterModelOptions(
            name='epoca',
            options={'verbose_name': 'Época', 'verbose_name_plural': 'Épocas'},
        ),
        migrations.AlterModelOptions(
            name='evento',
            options={'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'verbose_name': 'Persona', 'verbose_name_plural': 'Personas'},
        ),
        migrations.AlterModelOptions(
            name='persona_cargo',
            options={'verbose_name': 'Relación persona y cargo', 'verbose_name_plural': 'Relaciones de personas y cargos'},
        ),
        migrations.AlterModelOptions(
            name='relacion_persona',
            options={'verbose_name': 'Relacion entre personas', 'verbose_name_plural': 'Relaciones entre personas'},
        ),
        migrations.AlterModelOptions(
            name='tipoevento',
            options={'verbose_name': 'Tipo de evento', 'verbose_name_plural': 'Tipos de eventos'},
        ),
        migrations.RemoveField(
            model_name='persona',
            name='cargo',
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 28, 13, 11, 28, 652709)),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 28, 13, 11, 28, 651577)),
        ),
        migrations.AlterModelTable(
            name='cargo',
            table='cargo',
        ),
        migrations.AlterModelTable(
            name='dinastia',
            table='dinastia',
        ),
        migrations.AlterModelTable(
            name='epoca',
            table='epoca',
        ),
        migrations.AlterModelTable(
            name='evento',
            table='evento',
        ),
        migrations.AlterModelTable(
            name='persona',
            table='persona',
        ),
        migrations.AlterModelTable(
            name='persona_cargo',
            table='rel_persona_cargo',
        ),
        migrations.AlterModelTable(
            name='relacion_persona',
            table='rel_personas',
        ),
        migrations.AlterModelTable(
            name='tipoevento',
            table='tipo_evento',
        ),
    ]
