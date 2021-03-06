# Generated by Django 3.1.7 on 2021-02-28 10:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 28, 11, 58, 19, 288513)),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 28, 11, 58, 19, 287355)),
        ),
        migrations.CreateModel(
            name='Persona_Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ini', models.DateField(verbose_name='Fecha inicio')),
                ('ac_fini', models.BooleanField(default=False, verbose_name='Antes de cristo')),
                ('fecha_fin', models.DateField(blank=True, null=True, verbose_name='Fecha fin')),
                ('ac_ffin', models.BooleanField(default=False, verbose_name='Antes de cristo')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personas', to='web.cargo')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargos', to='web.persona')),
            ],
        ),
    ]
