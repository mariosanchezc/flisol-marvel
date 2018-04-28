from django.urls import path
from django.views.generic import TemplateView
from .views import prueba1, CreatePersonajeView, ListPersonajeView



app_name = "personajes"

urlpatterns = [
    path("", prueba1, name="prueba"),
    path("crear-personaje", CreatePersonajeView.as_view(), name="crear-personaje"),
    path("creado/", TemplateView.as_view(template_name="personajes/creado.html"), name="creado"),
    path("list-personajes/", ListPersonajeView.as_view(), name="list"),
]
