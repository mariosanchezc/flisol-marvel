from django.db import models

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
    imagen = models.ImageField()
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
