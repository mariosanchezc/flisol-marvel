from django.urls import path
from .views import prueba1, PruebaView



app_name = "personajes"

urlpatterns = [
    path("", prueba1, name="prueba"),
    path("prueba2", PruebaView.as_view(), name="prueba2")
]
