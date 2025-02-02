def tervehdi():
    print("Funktio tervehtii")
    return
# -- pääohjelma alkaa
print("Pääohjelma alkaa")
# kutsutaan funktiota
tervehdi()
print("Ohjelma loppu, näkemiin!")

#funktio joka saa alkuarvon eli parametrin
#Funktio ei palauta mitään.
def tuplaus(luku):
    print(f"Sain alkuarvoksi luvun {luku}")
    tulos = 2 * luku
    print (f"Alkuarvo eli parametrin arvo tuplana {tulos}")
#pääohjelma
tuplaus(3)
print("Ollaan takaisin pääohjelmassa")


def nelio(luku):
    tulos = luku ** 2
    #tulos = math.pow (luku, 2)
    #funktio palauttaa laskemansa arvon
    #muista ottaa arvo talteen!
    return tulos
arvo = float(input("Anna luku:\n"))
vastaus = nelio(arvo)
print((f"Lukusi neliö on:{vastaus}"))