from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.ForeignKey(
            User,
            related_name='user', verbose_name='Пользователь',
            on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100, verbose_name='Имя игрока')
    email = models.EmailField(verbose_name='Почтовый адрес')
    wishlist = models.TextField()
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
        null=True, blank=True,
    )
    price_limit = models.DecimalField(
        max_digits=9, decimal_places=2,
        default=1000, verbose_name='Стоимость подарка'
    )
    reg_date_limit = models.DecimalField(
        default='2021-12-30',
        verbose_name='Последний день регистрации'
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
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'



class GameCreator(models.Model):
    name = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    email = models.EmailField(verbose_name='Почтовый адрес')

    def __str__(self):
        return self.name.username

    class Meta:
        verbose_name = 'Создатель игры'
        verbose_name_plural = 'Создатели игры'


class Game(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название игры'
    )
    game_creator = models.ForeignKey(
        GameCreator, related_name='creator',
        verbose_name='Создатель',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=9, decimal_places=2,
        default=1000, verbose_name='Стоимость подарка'
    )
    draw_date = models.DateField(
        default='2021-12-31',
        verbose_name='Дата жеребьёвки'
    )
    gift_date = models.DateField(
        verbose_name='Дата отправки подарка'
    )
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class Player(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя участника')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class Registration(models.Model):
    player_name = models.ForeignKey(
        Player, related_name='player',
        verbose_name='Игрок',
        on_delete=models.CASCADE
    )

    interests = models.CharField(max_length=300, verbose_name='Интересы')
    letter = models.TextField(verbose_name='Письмо санте')
    slug = models.SlugField()

    def __str__(self):
        return self.player_name.name

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрации'


class Draw(models.Model):
    game = models.ForeignKey(
        Game, related_name='game_discription',
        verbose_name='Игра',
        on_delete=models.CASCADE
    )
    giver = models.ForeignKey(
        Player, related_name='gift_giver',
        verbose_name='Кто дарит',
        on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        Player, related_name='gift_recipient',
        verbose_name='Кому дарит',
        on_delete=models.CASCADE
    )

    # def __str__(self):
    # Кто кому дарит

    class Meta:
        verbose_name = 'Жеребьевка'
        verbose_name_plural = 'Жеребьевки'
