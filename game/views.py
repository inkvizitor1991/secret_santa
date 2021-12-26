import random

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django import views
from .forms import LoginForm, RegistrationForm, GameForm, PasswordForm
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
            game_password=int(password),
            game=game
        )
        return render(request, 'congratulations.html', {'password': password})




class PasswordGame(views.View):
    def get(self, request, *args, **kwargs):

        name = Player.objects.get(name='dr')
        game = Game.objects.get(name='а')
        name.creator.add(game)
        print(name.creator.all())
        print(name)
        print(game)

        form = PasswordForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'password_game.html', context)


    def post(self, request, *args, **kwargs):
        form = PasswordForm(request.POST or None)
        if form.is_valid():
            name = Player.objects.get(name='dr')
            game = Game.objects.get(id=int(request.user.id)) #?????
            #создаем игрока
            player = Player.get_or_create(
                user=request.user,
                name=request.user.name,
                email=request.mail,
                wishlist=str(form.cleaned_data['wishlist']),
                message_to_santa=form.cleaned_data['message_to_santa'],
            )

            GamePassword.objects.create(
                game_password=int(password),
                game=game
            )

            Game.players.add(player)


            return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(request, 'password_game.html', context)
