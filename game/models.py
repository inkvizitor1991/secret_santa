from django.db import models




class GameCreator(models.Model):
    name = models.CharField(
        max_length=100,
        default='Santa',
        verbose_name='Название создателя игры'
    )

    def __str__(self):
        return self.name

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
    email = models.EmailField(verbose_name='Почтовый адрес')
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
    objects = ResultQuerySet.as_manager()
    # def __str__(self):
    # Кто кому дарит

    class Meta:
        verbose_name = 'Жеребьевка'
        verbose_name_plural = 'Жеребьевки'
