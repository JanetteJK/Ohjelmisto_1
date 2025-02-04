#kuin lista mutta sama alkio voi esiintyä vain yhden kerran
#joukossa alkioilla ei ole järjestystä
#aaltosuluilla merkitään joukkoa
#koska joukolla ei ole järjestystä lisätään joukkoon käyttäen .add
import random

pelit = {"Monopoli", "Shakki", "Cluedo"}
print(pelit)

pelit.add("Dominion")
print(pelit)

pelit.remove("Shakki")
print(pelit)

pelit.add("Cluedo")
print(pelit)

for p in pelit:
    print(p)
#jos haluat luoda setin tyhjästä tämä on malli
nimet = set()
nimet.add("Viivi")
print(nimet)

arvotut = set()                             #arvotaan 4 eri lukua väliltä 1,9
while len(arvotut) < 4:                     #len = listan pituus
    uusi_luku = random.randint(1,9)   #ei tarvitse muuta koska kahta samaa numeroa ei voi olla
    arvotut.add(uusi_luku)
print(arvotut)
