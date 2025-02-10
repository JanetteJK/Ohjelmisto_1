import mysql.connector
def hae_tiedot():
    sql = f"select count(type), type from airport where iso_country='{maakoodi}'Group by type desc"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(f"{tulos}")

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='janetjk',
    password='niittykuja4MAR',
    autocommit=True
    )

maakoodi = input("Sano maan maakoodi:\n")
hae_tiedot()