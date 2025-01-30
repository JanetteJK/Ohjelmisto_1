import math
kanta_str = input(f"mikä on suorakulmion kanta")
kanta = float(kanta_str)
korkeus_str = input(f"mikä on suorakulmion korkeus")
korkeus = float(korkeus_str)
piiri = (kanta+kanta+korkeus+korkeus)
pintaala = (kanta*korkeus)
print (f"suorakulmion piiri on {piiri} ")
print (f"suorakulmion pinta-ala on {pintaala}")
