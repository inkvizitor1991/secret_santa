import datetime

from collections import deque
from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from textwrap import dedent

from game.models import Game, Player


def make_draw(game):
    santas = list(game.players.all().order_by('?'))
    if len(santas) < 1:
        print('Добавте игроков')
        return 0
    if santas[0].gift_reciever:
        print('Жеребьевка уже проведена')
        return 0
    for i, player in enumerate(santas):
        try:
            reciever = santas[i+1].email
            player.gift_reciever=reciever
            player.save()
        except IndexError as error:
            reciever = santas[0].email
            player.gift_reciever=reciever
            player.save()


def send_email(subject, to_addr, body_text):
    send_mail(
        subject,
        body_text,
        settings.DEFAULT_FROM_EMAIL,
        [to_addr],
        fail_silently=False,
    )


def make_and_send_email_message(game):
    subject = f'Жеребьевка в игре {game.name} проведена!'
    body_text = dedent(
        f"""Жеребьевка в игре {game.name} проведена!
        Спешу сообщить кто тебе выпал.
        Ваш игрок: draw.receiver.user.username
        Адрес эл. почты: draw.receiver.user.email
        Письмо Санте: draw.receiver.letter_to_santa
        Вишлист: draw.receiver.wishlist"""
    )
    send_email(subject, 'picture.jpg@yandex.ru', body_text)


#def is_date_valid(draw_date):
#    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
#    if draw_date >= current_date:
#        return True
#    return False
#
#        games = Game.objects.filter(draw_date=current_date)
#        for game in games:
#            make_draw(game)
#            make_and_send_email_message(game)
