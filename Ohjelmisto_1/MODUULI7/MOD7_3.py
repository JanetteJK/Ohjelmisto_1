lentokentät = {"EFHK":"Helsinki",
               "RJAA":"Narita",
               "RJOO":"Osaka",
               "WABI":"Nabire"}


def valikko():
    print ("Mitä haluat tehdä?")
    valinta = int(input(" 1 - Syötä uusi lentoasema\n 2 - Etsi lentoasemaa ohjelmasta\n 3 - Lopeta ohjelma\n"))
    return valinta

def syötä_uusi_asema():
    nimi = input("Anna aseman nimi: \n")
    icao = input("Anna aseman ICAO-koodi: \n")
    lentokentät[icao] = nimi
    print("Lentokenttä lisätty ohjelmaan.\n")



def etsi_asemaa():
    kenttä = input("Anna ICAO-koodi: \n")
    if kenttä in lentokentät:
        print (f"Koodia vastaava lentökenttä on {lentokentät[kenttä]}\n")


def sulje():
    print("Ohjelma suljetaan")

valinta = valikko()
while valinta != 3:
    if valinta == 1:
        syötä_uusi_asema()
        valinta = valikko()
    if valinta == 2:
        etsi_asemaa()
        valinta = valikko()
sulje()


