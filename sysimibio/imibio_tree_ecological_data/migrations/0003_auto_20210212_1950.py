# Generated by Django 3.1.3 on 2021-02-12 19:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('imibio_tree_ecological_data', '0002_auto_20201229_1232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='treeecologicaldata',
            options={'verbose_name': 'Campo', 'verbose_name_plural': 'Registro de campo'},
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='acompanantes',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='altura',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='clasificacion_sociologica',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='especie',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='estado_arbol',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='forma_vida',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='fotografia',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='hora_final',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='hora_inicio',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='humedad',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='id_arbol',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='id_parcela',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='latitud',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='longitud',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='responsable',
        ),
        migrations.RemoveField(
            model_name='treeecologicaldata',
            name='temperatura',
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='coordinator',
            field=models.CharField(default='Florencia', max_length=100, verbose_name='responsable'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 2, 12, 19, 48, 19, 234266, tzinfo=utc), verbose_name='fecha'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='end_time',
            field=models.TimeField(default='0:20', verbose_name='hora_final'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='humidity',
            field=models.FloatField(default=0, verbose_name='humedad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='latitude',
            field=models.FloatField(default=-26, verbose_name='latitud'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='life_form',
            field=models.CharField(default='', max_length=100, verbose_name='Forma de Vida'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='longitude',
            field=models.FloatField(default=-54, verbose_name='longitud'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='parcel_id',
            field=models.IntegerField(default=1, verbose_name='ID parcela'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='photo',
            field=models.URLField(blank=True, null=True, verbose_name='fotografia'),
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='sociological_classification',
            field=models.CharField(default='1', max_length=100, verbose_name='clasificación sociologica'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='specie',
            field=models.CharField(default='', max_length=100, verbose_name='especie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='staff',
            field=models.CharField(default='', max_length=100, verbose_name='acompanantes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='start_time',
            field=models.TimeField(default='0:00', verbose_name='hora_inicio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='temperature',
            field=models.FloatField(default=36, verbose_name='temperatura'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='tree_height',
            field=models.FloatField(default=6, verbose_name='Altura del árbol'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='tree_id',
            field=models.IntegerField(default=2, verbose_name='ID Árbol'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeecologicaldata',
            name='tree_status',
            field=models.CharField(default='1', max_length=100, verbose_name='Estado del árbol'),
            preserve_default=False,
        ),
    ]