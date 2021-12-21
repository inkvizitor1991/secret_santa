from django.contrib import admin

from .models import (
    GameCreator, Game,
    Player, Registration,
    Draw
)

admin.site.register(GameCreator)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Registration)
admin.site.register(Draw)