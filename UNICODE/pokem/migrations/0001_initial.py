# Generated by Django 3.1.7 on 2021-07-22 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('normal', 'normal'), ('fighting', 'fighting'), ('flying', 'flying'), ('poison', 'poison'), ('ground', 'ground'), ('rock', 'rock'), ('bug', 'bug'), ('ghost', 'ghost'), ('steel', 'steel'), ('fire', 'fire'), ('water', 'water'), ('grass', 'grass'), ('electric', 'electric'), ('psychic', 'psychic'), ('icedragon', 'icedragon'), ('darkfairy', 'darkfairy'), ('unknown', 'unknown'), ('shadow', 'shadow')], max_length=200)),
            ],
        ),
    ]
