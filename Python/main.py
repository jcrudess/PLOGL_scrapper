from plavi_oglasnik import PlaviOglasnik
import time
from utils import *
import requests

sess = getTorSession()
r = sess.get('http://httpbin.org/ip')
print (r.text)

loadID = startLoad()
print('load_id='+str(loadID))
plo = PlaviOglasnik(sess)
plo.start(loadID)