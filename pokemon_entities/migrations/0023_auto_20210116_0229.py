# Generated by Django 3.1.5 on 2021-01-15 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0022_auto_20210116_0220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='previous_evolution',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='next_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='previous_evolution', to='pokemon_entities.pokemon'),
        ),
    ]
