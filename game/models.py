from django.db import models
from game import choice_gift, choice_price_gift
from django.contrib.auth.models import User




class Player(models.Model):
    user = models.ForeignKey(
            User,
            related_name='user', verbose_name='Пользователь',
            on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100, verbose_name='Имя игрока')
    email = models.EmailField(verbose_name='Почтовый адрес')
    wishlist = models.CharField(blank=True, choices=choice_gift.CHOICES, max_length=500)
    message_to_santa = models.TextField(blank=True)
    gift_reciever = models.ForeignKey(
            'self',
            related_name='player_reciever',
            null=True, blank=True,
            on_delete=models.DO_NOTHING,
    )
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class Game(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название игры'
    )
    game_creator = models.ForeignKey(
        User,
        related_name='creator',
        verbose_name='Создатель',
        on_delete=models.CASCADE
    )
    game_creator_assistent = models.ManyToManyField(
        Player,
        related_name='creator_assistant',
        verbose_name='Помощник',
        blank=True,
    )
    price_limit = models.CharField(
        blank=True, choices=choice_price_gift.CHOICES,
        verbose_name='Стоимость подарка', max_length=5, null=True
    )
    draw_date = models.DateField(
        default='2021-12-31',
        verbose_name='Дата жеребьёвки'
    )
    gift_date = models.DateField(
        verbose_name='Дата отправки подарка'
    )
    players = models.ManyToManyField(
            Player,
            related_name='games',
            blank=True,
    )
    invitation_email = models.EmailField(verbose_name='Почта для отправки приглашения',blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'



class GamePassword(models.Model):
    game_password = models.IntegerField(
        verbose_name='Пароль для входа в игру',

    )
    game = models.OneToOneField(
        Game,
        related_name='game',
        verbose_name='Игра',
        on_delete=models.CASCADE,

    )

    slug = models.SlugField()

    def __str__(self):
        return str(self.game)

    class Meta:
        verbose_name = 'Пароли'
        verbose_name_plural = 'Пароль'

