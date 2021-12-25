import random

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django import views
from .forms import LoginForm, RegistrationForm, GameForm
from .models import Game, Player, GamePassword


class BaseViews(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', {})


class LoginView(views.View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(request, 'login.html', context)


class RegistrationView(views.View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'registration.html', context)

    def post(self, request, *args, **kwargs):

        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Player.objects.create(
                user=new_user,
                name=new_user,
                wishlist=form.cleaned_data['wishlist'],
                message_to_santa=form.cleaned_data['message_to_santa'],
                email=form.cleaned_data['email'],
            )
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(request, 'registration.html', context)


class AccountView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'account.html', {})


class GameView(views.View):

    def get(self, request, *args, **kwargs):
        games = Game.objects.all()
        return render(request, 'game.html', {'games': games})


class CreateGameView(views.View):

    def get(self, request, *args, **kwargs):
        form = GameForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'create_game.html', context)

    def post(self, request, *args, **kwargs):
        form = GameForm(request.POST or None)
        if form.is_valid():
            Game.objects.create(

                name=form.cleaned_data['name'],
                draw_date=form.cleaned_data['draw_date'],
                price_limit=form.cleaned_data['price_limit'],
                reg_date_limit=form.cleaned_data['reg_date_limit'],
                gift_date=form.cleaned_data['gift_date'],
                game_creator=request.user
            )
            return HttpResponseRedirect('/congratulations/')
        context = {
            'form': form
        }
        return render(request, 'create_game.html', context)


class Congratulations(views.View):
    def get(self, request, *args, **kwargs):
        password = random.randint(1, 999999)
        game = Game.objects.all().last()
        GamePassword.objects.create(
            password=int(password),
            game=game
        )
        return render(request, 'congratulations.html', {'password': password})




gifts = [
        'Новый смартфон.',
        'Настольная игра.',
        '5-10 килограммов мандаринов (для кого-то это настоящее счастье).',
        'Планшет.',
        'Сертификат в парк развлечений.',
        'Билеты в кино.',
        'Билеты на каток.',
        'Графический планшет.',
        'Книга.',
        'Сертификат на развивающий курс.',
        'Набор для творчества.',
        'Картина.',
        'Сертификат какого-либо магазина.',
        'Компьютерная игра.',
        'Персональный компьютер.',
        'Ноутбук.',
        'Запчасти для персонального компьютера (видеокарта, монитор и т. д.)',
        'Алкоголь.',
        'Портсигар.',
        'Ювелирные изделия.',
        'Мягкая игрушка.',
        'Набор подарочных конфет.',
        'Домашнее животное.',
        'Головоломка.',
        'Портативная зарядка.',
        'Bluetooth-наушники.',
        'Сертификат в салон красоты.',
        'Чай, кофе, горячий шоколад.',
        'Шарф, шапка и варежки.',
        'Билет на концерт.',
        'Путевка в другой город или страну.',
        'Термокружка.',
        'Сертификат на татуировку.',
        'Деньги.',
        'Снежный шар.',
        'Подарочные наборы личной гигиены.',
        'Сертификат на фотосессию.',
        'Бытовые приборы (утюг, чайник, посуда и т.д.)',
        'Игровая приставка.',
        'Полароид.',
        'Кружка.',
        'Копилка.',
        'Блокнот, ежедневник, скетчбук.',
        'Духи или парфюм.',
        'Дорожная подушка.',
        'Настольный светильник.',
        'Свитшот, футболка.',
        'Портативная колонка.',
        'Чайный сервиз.',
        'Наборы для выращивания растений.',
]


class WishlistView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'wishlist.html', {'gifts': gifts})



class HowtoView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'how_to.html', {})

