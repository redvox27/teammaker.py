import urllib.request
import requests
import urllib.parse
from bs4 import BeautifulSoup
import unicodedata
import webbrowser
import time

class Scraper():
    def __init__(self):
        print("init")




    def spider(self):
        url = "http://pokeunlock.com/pokedex/pokemon-with-base-stats/"


        headers = {}
        headers["User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

        req = requests.get(url,headers=headers)
        plain_text = req.text
        soup = BeautifulSoup(plain_text)
        linkList = []

        for pokemonlink in soup.findAll("a"):
            if "non" not in pokemonlink:
                href = pokemonlink.get("href")

            try:
                if "/pokedex" in href and href.islower() and "http" not in href:
                    href = "http://pokeunlock.com" + href
                    Scraper.get_stats(self,href)
                    linkList.append(href)


            except Exception as f:
                f = 0

        print(linkList)
        list(set(linkList))


    def get_stats(self,url):
        headers = {}
        headers["User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

        req = requests.get(url, headers=headers)
        plain_text = req.text
        soup = BeautifulSoup(plain_text)
        link_list = []

        print(url)
        for stat in soup.findAll("mark",{"class":"x-highlight dark"}):
            print(stat)
            link_list.append(stat)

        print(link_list)




test = Scraper()
test.spider()

