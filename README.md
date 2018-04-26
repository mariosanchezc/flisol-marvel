## FIRST APPS 
Esta rama Soluciona el reto 2 (Creación de APPS y Modelo Personaje):

1. Crear una carpeta apps
    - mkdir apps
2. Dentro de la carpeta apps crear una nueva app
    - django-admin startapp <personajes>
3. Instalar nuestra app personajes:
    - dentro del archivo settings en OWNER_APPS
4. Crear nuestro primer modelo
    - Escribe su modelo Personaje dentro del archivo models.py
5. Hacer Migraciones
    - python manage.py makemigrations
    - python manage.py migrate
6. Referencias: 
    - https://docs.djangoproject.com/en/2.0/topics/db/models/