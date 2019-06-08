import requests
from bs4 import BeautifulSoup
from utils import *
from Oglas import Oglas

class PlaviOglasnik:
    moduleName = 'PLAVI OGLASNIK'
    brojStranica = 1
    url = ''

    def __init__(self):
        self.url = 'https://www.oglasnik.hr/stanovi-najam?page='
        #headers = {}

    def start(self, loadID):
    #     print(data['href'].split('-')[-1]) #id oglasa iz linka - provjeriti da li postoji u bazi prije kreiranja
    #     objeka radi čuvanja memorije
        for i in range(1, self.brojStranica + 1):
            stranica = str(i)
            r = requests.get(self.url+stranica)
            print(self.moduleName + ': radim stranicu '+stranica)

            soup = BeautifulSoup(r.text, "html.parser")

            data = soup.select('div a.ad-box')
            for link in data:
                lolID = insertLink(link['href'], loadID, self.moduleName, link['href'].split('-')[-1])
                #ako je oglID = 1 znači da oglas postoji u bazi pa ne treba ništa raditi
                if (lolID != 1):
                    #otiđi na stranicu oglasa i popuni podatke                                        
                    oglas = self._kreirajOglas(link['href'], lolID)
                    if oglas is None:
                        continue
                    else:
                        insertOglas(oglas)
                        del oglas
                else:
                    print('nije unesen jer već postoji!')

    def _kreirajOglas(self, link, lolID):
        r = requests.get(link)
        soup = BeautifulSoup(r.text, "html.parser")
        try:
            cijenaTag = soup.select('span.price-oglas-details')#[0].string.replace('.', '').split(' ')[1]
            if not cijenaTag:
                cijena = 0#odrediCijenu(soup)
            else:
                cijena = cijenaTag[0].string.replace('.', '').split(' ')[1]
            datum = soup.select('span.hidden-sm b')[0].string.split(' ')[1]
            slikeList = []
            for link in soup.select('ul.thumbnails li'):
                slikeList.append('http://www.oglasnik.hr' + link['data-fullscreen-url'])
            if not slikeList:
                print('nema slika!')
            return Oglas(link, cijena, datum, slikeList, lolID)
        except Exception as e:
            print('oglas '+link+' nije unesen! Error: ')
            print (e)

    
        