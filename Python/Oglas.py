import requests
from bs4 import BeautifulSoup
class Oglas:
    link = ''
    cijena = 0
    datumOglasa = ''
    imgLinks = []
    def __init__(self, link, cijena, datumOglasa, imgLinks, lolID):
        self.link = link
        self.cijena = cijena
        self.datumOglasa = datumOglasa
        self.imgLinks = imgLinks
        self.lolID = lolID



