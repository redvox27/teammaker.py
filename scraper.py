import urllib.request
import requests
import urllib.parse
from bs4 import BeautifulSoup
import webbrowser
import time

class Scraper():


    def __init__(self,url):
        self.url = url

        #lege constructor
        #lege contructor

    def spider(self):


        headers = {}
        headers["User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

        req = requests.get(self.url,headers=headers)
        plain_text = req.text
        soup = BeautifulSoup(plain_text)

        for pokemonlink in soup.findAll("a",{"class":"column-3"}):
            href = "http://pokeunlock.com/pokedex" + pokemonlink.get("href")
            title = pokemonlink.sting
            print(href)
            print(title)
        print(href)
test = Scraper("http://pokeunlock.com/pokedex/pokemon-with-base-stats/")
test.spider()