# Generated by Django 4.0 on 2021-12-26 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_remove_game_reg_date_limit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamepassword',
            old_name='password',
            new_name='game_password',
        ),
    ]
