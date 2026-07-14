"""
Sistema de análisis de noticias con APIS múltiples.
"""

# PEP8: configuracion centralizada - constante en MAYUSCULAS
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "sl"


# PEP8: utilidades comunes del proyecto - funciones en snake_case
def clean_text(text):
    # PEP8: 4 espacios por identacion no tabs
    """Limpia y normaliza texto"""  # PEP8: Docsstrings


API_KEY = "9f813cdcac4b4b2ea394637ff93324cd"
BASE_URL = "https://newsapi.org/v2/everything"

import json
import urllib
import urllib.parse
import urllib.request


class NewsSystemError(Exception):
    """Error general en la app"""

    pass


class APIKeyError(NewsSystemError):
    """Error  cuando la API KEY es invalida"""

    pass


def newapi_client(api_key, query, timeout=30, retries=3):
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    print(query_string)

    url = f"{BASE_URL}?{query_string}"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError:
        raise APIKeyError("Ocurrio un error no se pudo conectar con la API")

    return f"NewApi; {query} con timeput {timeout}"


def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con timeout {timeout}"


def ejemplo_args(api_key, *args):
    print(f"api_key {api_key}")
    print(f"args {args}")
    print(f"{type(args)}")
    print("======")


ejemplo_args("APY_KEY_VALUE", "Este", "parametro", "aca")

"""
Kwargs
"""


def ejemplo_kwargs(**kwargs):
    print(f"kwargs: {type(kwargs)}")
    print(f"kwargs:{kwargs}")
    print("=======")


ejemplo_kwargs(
    apikey="DEMO_GUARDIAN",
    section="sports",
    from_date="202-10-10",
    timeout=30,
    retries=3,
)


def fetch_news(api_name, *args, **kwargs):
    """
    Función felxible para conectar con la API
    """
    base_config = {
        "timeout": 30,
        "retries": 3,
    }

    config = {**base_config, **kwargs}

    api_clients = {
        "newapi": newapi_client,
        "guardian": guardian_client,
    }

    client = api_clients[api_name]
    return client(*args, **config)


response_data = None
try:
    response_data = fetch_news("newapi", api_key=API_KEY, query="Python")
    print(response_data)
except APIKeyError as e:
    print(f"Ocurrio un errro: {e}")
if response_data:
    for article in response_data["articles"]:
        print(article["title"])
