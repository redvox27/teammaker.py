import urllib.request
import requests
import urllib.parse
from bs4 import BeautifulSoup
import webbrowser
import time

def spider():
    page = 0


    url = "http://pokeunlock.com/pokedex/pokemon-with-base-stats/"
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    req = requests.get(url, headers=headers)

    plain_text = req.text

    soup = BeautifulSoup(plain_text)
    pokemon_lis = []
    for link in soup.findAll("a"):
         href = link.get("href")

         try:

            if "/pokedex/" in href and not "http://" in href:
                pokemon_lis.append(href.lower())


         except Exception as f :
             f = 0

    pokemon_lis = list(set(pokemon_lis))
    print(pokemon_lis)
    print(len(pokemon_lis))
spider()