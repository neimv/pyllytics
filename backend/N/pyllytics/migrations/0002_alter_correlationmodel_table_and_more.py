# Generated by Django 4.0.2 on 2022-02-14 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyllytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='correlationmodel',
            table='correlation',
        ),
        migrations.AlterModelTable(
            name='descriptivestatisticsmodel',
            table='descriptive_statistics',
        ),
        migrations.AlterModelTable(
            name='sourcemodel',
            table='source',
        ),
        migrations.AlterModelTable(
            name='sourcetypesmodel',
            table='source_types',
        ),
    ]
