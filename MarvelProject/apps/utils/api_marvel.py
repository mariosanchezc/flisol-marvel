import hashlib
import requests
from .keys import PUBLIC_KEY, PRIVATE_KEY


URL_MARVEL = "https://gateway.marvel.com:443/v1/public/characters?apikey={}".format(PUBLIC_KEY)

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
                                  'hash': hash_clave}).json()
    data = personajes.results
    