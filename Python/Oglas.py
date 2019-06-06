import requests
from bs4 import BeautifulSoup
from utils import insert
class Oglas:
    idOglasa = 0
    link = ''
    imgLink = ''
    cijena = 0
    datumOglasa = ''
    povrsina = 0
    lokacija = ''
    def __init__(self, link, headers, idOglasa):
        self.link = link
        self.idOglasa = idOglasa
        r = requests.get(link, headers)
        soup = BeautifulSoup(r.content, "html.parser")



