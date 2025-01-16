nimi = "Janette"
print ("Moi "  + nimi + ", mitä kuuluu?")
print(f"moi {nimi}, kuinkas nyt menee?")

# käyttäjän syötteen lukeminen
# huom: input lukee kaikki syötteet
# aina merkkijonoina
lukuA_str = input("anna kokonaisluku")
lukuA = int(lukuA_str)
# luen käyttäjän suoraa lukuna
lukuB = int(input("anna toinen luku: "))
summa = lukuA + lukuB

print (f"lukujesi summa = {summa}")