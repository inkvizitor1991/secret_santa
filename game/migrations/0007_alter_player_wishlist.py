# Generated by Django 4.0 on 2021-12-24 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_remove_gamecreator_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='wishlist',
            field=models.TextField(blank=True),
        ),
    ]
