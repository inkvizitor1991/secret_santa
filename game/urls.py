from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    BaseViews, RegistrationView,
    LoginView, AccountView,
    CreateGameView, GameView,
    Congratulations, WishlistView
)




urlpatterns = [
    path('',BaseViews.as_view(), name='base'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('account/', AccountView.as_view(), name='account'),
    path('create/', CreateGameView.as_view(), name='create'),
    path('game/', GameView.as_view(), name='game'),
    path('congratulations/', Congratulations.as_view(), name='congratulations'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),


]