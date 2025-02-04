viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")

numerot = 1,2,3
print (numerot)

eka, toka, kolmas = numerot
#katsoo ensin vasemmalta mistä kyse, sitten ottaa oikealta puolelta termit ja yhdistää ne monikkoon
#printtaisi siis ylemmässä print eka : 1

import random

def heitä():
    eka, toka = random.randint(1,6), random.randint(1,6)
    return eka, toka

noppa1, noppa2 = heitä()
print(f"Nopista tuli {noppa1} ja {noppa2}.")
#jos haluaa palauttaa funktiosta useamman arvon tämä on hyvä tapa