from send_message import send_message_to_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django import views

from .forms import LoginForm, RegistrationForm, GameForm, PasswordForm, CongratulationsForm

from .forms import (
        LoginForm,
        RegistrationForm,
        GameForm,
        PasswordForm,
        ButtonForm
)

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
        player = Player.objects.get(name=request.user)
        return render(request, 'account.html', {'player': player})


class GameView(views.View):

    def post(self, request, *args, **kwargs):
        form = ButtonForm(request.POST or None)
        games = Game.objects.all()
        draw.make_draw(games[0])
        draw.make_and_send_email_message(games[0])
        return render(request, 'game.html', {'games': games})

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




class PasswordGame(views.View):
    def get(self, request, *args, **kwargs):
        form = PasswordForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'password_game.html', context)

    def post(self, request, *args, **kwargs):
        form = PasswordForm(request.POST or None)

        if form.is_valid():
            game_password = GamePassword.objects.get(
                game_password=form.cleaned_data['game_password'])
            game = Game.objects.get(name=game_password)
            name = Player.objects.get(name=request.user)

            name.wishlist = form.cleaned_data['wishlist']
            name.save()
            name.message_to_santa = form.cleaned_data['message_to_santa']
            name.save()
            name.creator_assistant.add(game)

            return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(request, 'password_game.html', context)



class Congratulations(views.View):

    def get(self, request, *args, **kwargs):
        game = Game.objects.all().last()
        password = game.id
        GamePassword.objects.update_or_create(
            game_password=int(password),
            game=game
        )
        form = CongratulationsForm(request.POST or None)
        context = {
            'form': form,
            'password': password
        }

        return render(request, 'congratulations.html', context)

    def post(self, request, *args, **kwargs):
        form = CongratulationsForm(request.POST or None)

        if form.is_valid():
            website = 'fdfdfsds'
            recipient_name = form.cleaned_data['receive_name']
            recipient_email = form.cleaned_data['invitation_email']
            send_message_to_mail(recipient_email)################тут функция которая отправляет сообщение на почту

            return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(request, 'congratulations.html', context)
