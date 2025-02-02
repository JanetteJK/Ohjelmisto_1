#while toistorakenne joka tulostaa kolmella jaolliset luvut 1....1000

luku = 1
while luku <= 1000:
    if luku % 3 == 0:   #jos jäännösluku on 0 sen jälkeen kun jaettu kolmella
        print(luku)
    luku += 1  #luku =luku + 1
print ("Homma tehty!")