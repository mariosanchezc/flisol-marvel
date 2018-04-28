import hashlib
import requests
from .keys import PUBLIC_KEY, PRIVATE_KEY

URL_MARVEL = "https://gateway.marvel.com:443/v1/public/characters?apikey={}".format(PUBLIC_KEY)


class PersonajeMarvel():
    def __init__(self, *args, **kwargs):
        self.nombre = args[0]
        self.imagen_url = args[1]
        self.descripcion = args[2]
        self.url = args[3]

    @property
    def imagen_url(self):
        return self.__imagen_url

    @imagen_url.setter
    def imagen_url(self, url):
        """
        de esta manera regresa marvel la Url de la Imagen
        {'path': 'http://i.annihil.us/u/prod/marvel/i/mg/c/e0/535fecbbb9784', 
         'extension': 'jpg'}
        """
        self.__imagen_url = url['path'] + '.' + url['extension']

def get_data():
    """
    Obtiene de la API de Marvel
    los Personajes.
    """
    ts = '1'
    hash_clave = hashlib.md5((ts + PRIVATE_KEY + PUBLIC_KEY).encode()).hexdigest()
    base = 'http://gateway.marvel.com/v1/public/'
    personajes = requests.get(base + 'characters',
                          params={'apikey': PUBLIC_KEY,
                                  'ts': ts,
                                  'hash': hash_clave,
                                  'limit':100}).json()
    data = personajes["data"]["results"]
    results = []
    for personaje in data:
        args = [personaje["name"], personaje['thumbnail'],
                personaje['description'], personaje['resourceURI']]
        per = PersonajeMarvel(*args)
        results.append(per)
    return results