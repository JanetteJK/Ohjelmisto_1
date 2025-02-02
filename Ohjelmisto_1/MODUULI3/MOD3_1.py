import math
kuhapituus = float(input("Mikä on kuhan pituus?:"))
sentit = int(37)
senttiä = (sentit-kuhapituus)
if kuhapituus >=37:
    print ("Sopivan kokoinen kuha kotiin vietäväksi!")
else:
    print (f"Kuha on {senttiä} senttiä liian pieni, heitä se pois.")