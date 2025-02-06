import _mysql_connector

def hae_kentan_tiedot(icao):
    sql = f"SELECT name FROM airport where ident='{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentoaseman nimi on {rivi[0]}")
    else:
        print("ICAO-koodillasi ei löytynyt lentoasemaa.")
