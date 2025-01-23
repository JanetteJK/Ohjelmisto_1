kt = "python"
ss = "rules"
kirjautumisyritykset = 0

kayttaja = input("Syötä käyttäjätunnus\n")
salasana = input("Syötä salasana\n")
while salasana!= ss or kayttaja!= kt:
    kirjautumisyritykset = kirjautumisyritykset +1
    print("Väärä käyttäjätunnus tai salasana!")
    if kirjautumisyritykset>4:
            print("Syötit väärät tunnukset liian monta kertaa,pääsy evätty!")
            break
    kayttaja = input("Syötä käyttäjätunnus\n")
    salasana = input("Syötä salasana\n")
if kayttaja == kt and salasana == ss:
    print("Tervetuloa")