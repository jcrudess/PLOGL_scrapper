from plavi_oglasnik import PlaviOglasnik
import time
from utils import startLoad

# while 1:
#     time.sleep(5)
# PlaviOglasnik()
loadID = startLoad()
print('load_id='+str(loadID))
PlaviOglasnik(loadID)