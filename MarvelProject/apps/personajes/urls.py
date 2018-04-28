from django.urls import path
from .views import prueba1


app_name = "personajes"

urlpatterns = [
    path("", prueba1, name="prueba")
]
