# Generated by Django 3.1.7 on 2021-08-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokem', '0012_pokemondata_u_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemondata',
            name='image',
        ),
        migrations.AddField(
            model_name='pokemondata',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]