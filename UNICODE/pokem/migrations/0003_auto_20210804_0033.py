# Generated by Django 3.1.7 on 2021-08-03 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokem', '0002_pokemondata_pokemons'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemondata',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemondata',
            name='weight',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
