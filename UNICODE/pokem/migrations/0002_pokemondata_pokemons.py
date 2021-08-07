# Generated by Django 3.1.7 on 2021-08-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]