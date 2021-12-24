from django.contrib import admin

from .models import (
    Game,
    Player,
#    GameCreator,
#    Registration,
#    Draw
)

admin.site.register(Game)
admin.site.register(Player)

#admin.site.register(GameCreator)
#admin.site.register(Registration)
#admin.site.register(Draw)
