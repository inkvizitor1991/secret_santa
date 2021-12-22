# Generated by Django 4.0 on 2021-12-22 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('game', '0004_registration_user_alter_player_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='email',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='user',
        ),
        migrations.AddField(
            model_name='gamecreator',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='Почтовый адрес'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gamecreator',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Пользователь'),
        ),
    ]