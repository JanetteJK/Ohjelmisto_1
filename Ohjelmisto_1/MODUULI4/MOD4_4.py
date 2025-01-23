import random
luku = random.randint (1,10)
pelaaja = int(input("Arvaa lukua:\n"))
while pelaaja>luku:
    print("Liian korkea")
    pelaaja = int(input("Arvaa lukua"))
while pelaaja<luku:
    print("Liian matala")
    pelaaja = int(input("Arvaa lukua"))
if pelaaja == luku:
    print("Oikea luku, onnittelut!")