# Generated by Django 4.0 on 2021-12-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_alter_gamepassword_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='wishlist',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('Новый смартфон.', 'Новый смартфон.'), ('2', 'Настольная игра.'), ('3', '5-10 килограммов мандаринов (для кого-то это настоящее счастье).'), ('4', 'Планшет.'), ('5', 'Сертификат в парк развлечений.'), ('6', 'Билеты в кино.'), ('7', 'Билеты на каток.'), ('8', 'Графический планшет.'), ('9', 'Книга.'), ('10', 'Сертификат на развивающий курс.'), ('11', 'Набор для творчества.'), ('12', 'Картина.'), ('13', 'Сертификат какого-либо магазина.'), ('14', 'Компьютерная игра.'), ('15', 'Персональный компьютер.'), ('16', 'Ноутбук.'), ('17', 'Запчасти для персонального компьютера'), ('18', 'Алкоголь.')]),
        ),
    ]