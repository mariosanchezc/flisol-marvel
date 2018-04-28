from django.db import models
from apps.utils.utils import user_directory_path
from django.urls import reverse


HEROE = "HEROE"
VILLANO = "VILLANO"

TIPOS = (
    (HEROE, "HEROE"),
    (VILLANO, "VILLANO")
)


class Personaje(models.Model):
    """
    Personajes de Marvel: Ejemplo: Wolverine
    """
    nombre = models.CharField(max_length=200)
    tipo_personaje = models.CharField(max_length=200, choices=TIPOS)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    imagen_url = models.URLField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


    def get_absolute_url(self):
        return reverse('personajes:detail', kwargs={'pk': self.pk})



class Comic(models.Model):
    """
    Un personaje puede estar en muchos Comics,
    Y un Comic puede tener muchos personajes
    """
    nombre = models.CharField(max_length=200)
    url = models.URLField()
    personajes = models.ManyToManyField(Personaje)

    def __str__(self):
        return self.nombre
