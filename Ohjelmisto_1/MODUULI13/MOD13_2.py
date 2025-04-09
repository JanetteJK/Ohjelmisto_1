import mysql.connector
from flask import Flask


app = Flask(__name__)
@app.route('/lentokentta/<icao>')

def hae_kentan_tiedot(icao):
    sql = f"SELECT name, municipality FROM airport where ident='{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            icao = icao
            nimi = rivi[0]
            kaupunki = rivi[1]
            answer = {
                'Icao': icao,
                'Name': nimi,
                'Municipality': kaupunki
            }
            return answer

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='niittykuja4MAR',
    autocommit=True
    )

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)