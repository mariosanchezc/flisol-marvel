from django.contrib import admin
from apps.personajes.models import Personaje, Comic

admin.site.register(Comic)
admin.site.register(Personaje)

