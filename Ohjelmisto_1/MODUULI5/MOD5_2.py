luvut = []
luku = str(input("Anna ensimmäinen luku tai paina Enter lopettaaksesi:\n"))
while (luku!= ""):
    luku = int(luku)
    luvut.append(luku)
    luku = str(input("Anna seuraava luku tai paina Enter lopettaaksesi:\n"))
luvut.sort(reverse=True)
print (luvut[0:5])