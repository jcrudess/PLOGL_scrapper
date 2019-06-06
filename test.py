import requests
from bs4 import BeautifulSoup

master_url = 'https://www.oglasnik.hr/stanovi-najam?ad_location_2%5B%5D=7442&ad_params_uploadable=1&ad_price_to=3.500'

while True:
    url = master_url + '&page={}'.format(counter)
    counter += 1
    print('radim url ' + url)
    site = requests.get(url)
    if (site.status_code != 200):
        print('Greška! Reponse code = ' + site.status_code)
    else:
        soup = BeautifulSoup(site.content)
        for item in soup.select('div a.ad-box'):
            print('cijena: ' + item.select('div.price-block')[0].select('span.price-kn')[0].get_text())
            print('datum objave '+ item.select('div span.date')[0].get_text())

#for item in soup.select('div a.ad-box'):
#    print(item['href'] + ', cijena: ' + item.select('div.price-block')[0].select('span.price-kn')[0].get_text())