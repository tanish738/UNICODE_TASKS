# Generated by Django 3.1.7 on 2021-08-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokem', '0004_pokemondata_move'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemondata',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
