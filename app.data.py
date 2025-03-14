import requests
import time
import os
import pandas as import pd


# URL PÚBLICA DE STAR WARS
base_url = "https://swapi.dev/api/"


# ENDPOINT PARA OBTER AS INFORMAÇÕES
films_endpoint = "films/"


# REQUISIÇÃO GET
response = requests.get(base_url + films_endpoint)


# VERIFICANDO RETORNO DA REQUISIÇÃO
if response.status_code == 200:
    data = response.json()
    for film in data['results']:
        print(f"Title: {film['title']}")
        print(f"Episode: {film['episode']}")
        print(f"Director: {film['director']}")
        print(f"Producer: {film['producer']}")
        print(f"Release Date: {film['release_date']}")
        print("-" * 30)
else:
    print(f"Erro: {response.status_code}")