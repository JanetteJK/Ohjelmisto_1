nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla enter:\n")
while nimi!="":
    nimet.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta painamalla Enter:\n")

print(nimet)