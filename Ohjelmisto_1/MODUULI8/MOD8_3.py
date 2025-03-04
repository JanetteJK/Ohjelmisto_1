import geopy
import mysql.connector

def distance():
    



def airports():
    airport_one = input("Anna ensimmäisen lentokentän ICAO-koodi:\n")
    airport_two = input("Anna toisen lentokentän ICAO-koodi:\n")
    return airport_one, airport_two

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='janetjk',
    password='niittykuja4MAR',
    autocommit=True
    )

def main():