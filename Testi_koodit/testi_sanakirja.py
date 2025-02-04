#TÄRKEÄ
#jos error koodi on KeyError, on jotain kirjoitettu väärin
#avain-arvopari, eli oikealla avaimella vedetään oikeaa tietoa
# {} <-- tyhjä sanakirja
#ensin kirjoitetaan avain, nyt nimi, sitten : ja se arvo mihin se johtaa
numerot = {"Viivi":"050-1234567",
           "Ahmed":"040-1112223",
           "Pekka":"050-7654321"}
#jos halutaan lisätä dataa: ["avain"] = "arvo"
numerot["Olga"] = "050-1011012"
numerot["Mary"] = "0401-2132139"

print (numerot)

nimi = input("Anna nimi: ").capitalize()#tekee aina inputista isolla kirjaimella alkavan
if nimi in numerot:
    print (f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")