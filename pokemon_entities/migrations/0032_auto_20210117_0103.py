# Generated by Django 3.1.5 on 2021-01-16 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0031_auto_20210117_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(default=0.0, verbose_name='широта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lon',
            field=models.FloatField(default=0.0, verbose_name='долгота'),
            preserve_default=False,
        ),
    ]