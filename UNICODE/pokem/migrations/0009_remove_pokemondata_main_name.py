# Generated by Django 3.1.7 on 2021-08-04 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokem', '0008_pokemondata_main_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemondata',
            name='main_name',
        ),
    ]