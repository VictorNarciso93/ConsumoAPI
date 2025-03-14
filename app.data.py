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