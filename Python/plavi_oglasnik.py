import requests
from bs4 import BeautifulSoup
from utils import *

moduleName = 'PLAVI OGLASNIK'
brojStranica = 1

def PlaviOglasnik(loadID):

    url = 'https://www.oglasnik.hr/stanovi-najam?page='
    #headers = {}   
    postojiUBazi = 0 

#     print(data['href'].split('-')[-1]) #id oglasa iz linka - provjeriti da li postoji u bazi prije kreiranja
#     objeka radi čuvanja memorije
    for i in range(brojStranica):
        stranica = str(i)
        r = requests.get(url+stranica)
        print(moduleName + ': radim stranicu '+stranica)

        soup = BeautifulSoup(r.text, "html.parser")

        data = soup.select('div a.ad-box')
        for link in data:
            postojiUBazi = insertLink(link['href'], loadID, moduleName, link['href'].split('-')[-1])
            # print(link['href'].split('-')[-1])


#ads-list > a:nth-child(2) > div.pad-xs-only-lr > h3