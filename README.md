## FIRST APPS 
SOLUCIÓN RETO 3: Creación de APPS y Modelos Personaje y Comic:

1. Crear una carpeta apps
    - mkdir apps
2. Dentro de la carpeta apps crear una nueva app
    - django-admin startapp <personajes>
3. Instalar nuestra app personajes:
    - dentro del archivo settings en OWNER_APPS
4. Crear nuestros primeros modelos
    - Escriba sus modelos: Personaje, Comic dentro del archivo models.py
5. Hacer Migraciones
    - python manage.py makemigrations
    - python manage.py migrate
6. Agregar al admin de django
    - Añadir el modelo Personaje al admin.py
7. Abrir la consola y ejecutar querysets
    - python manage.py shell
8. Referencias:
    - https://docs.djangoproject.com/en/2.0/topics/db/models/

## Reto 4:
Crea tu primera vista: La vista deberá renderizar un Template
y se deberá usar materialize para estilizar su plantilla.
