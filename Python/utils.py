import cx_Oracle as oracle 
from stem import Signal
from stem.control import Controller
import requests
import time
import re

def getTorSession():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
        print('čekam')
        time.sleep(controller.get_newnym_wait())
        print('DOOOOOČEEEEKO SAM PRIZNAJEEEEM TI SADAAAAA')

    sess = requests.session()
    sess.proxies = {}

    sess.proxies['http'] = 'socks5h://127.0.0.1:9050'
    sess.proxies['https'] = 'socks5h://127.0.0.1:9050'

    sess.cookies.clear()

    headers = {}
    headers['User-agent'] = "Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0"
    sess.headers = headers

    return sess

def connect():
    dsn = oracle.makedsn('localhost', '1521', 'xe')
    conn = oracle.connect(user = 'PLOGL_scrapper', password = 'PLOGLscrapper11', dsn=dsn)

    c = conn.cursor()

    return c

def startLoad():
    c = connect()
    loadId = c.var(oracle.NUMBER)
    print('pozivam utility.p_start_load')
    c.callproc('utility.p_start_load', [loadId])
    loadIdRet = int(loadId.getvalue())
    return loadIdRet

def insertLink(link, loadID, module, sifra):
    c = connect()
    id = c.var(oracle.NUMBER)
    c.callproc('utility.p_insert_load_link', [link, loadID, module, sifra, id])
    return int(id.getvalue())

def insertOglas(oglas):
    c = connect()
    oglID = c.var(oracle.NUMBER)
    slikeLinks = c.arrayvar(oracle.STRING, oglas.imgLinks)
    c.callproc('utility.p_insert_oglas', [oglas.lolID, oglas.cijena, oglas.datumOglasa, slikeLinks, oglID])


def odrediCijenu(soup):
    x = re.search("[0-9.,]+\s?(kn|KN|kuna|kune|Kuna|Kune|KUNA|KUNE|KUN|Kun|kun|\u20AC|EUR|eur|eura|EURA|Eura|Eur)", soup.text).group()
    print(x)
    if not x:
        cijena = 0
        print(cijena)
    else:
        cijena = re.search('[0-9]+',x.replace(',', '').replace('.', '').replace(' ','')).group()
        if (int(cijena) < 1000):
            #vjerovatno euri pa pomnoži sa 7.5
            print('euri')
            cijena = int(int(cijena)*7.5)
        print(cijena)
    print('-------------------------------------')
    return cijena
