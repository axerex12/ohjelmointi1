from geopy import distance
import mysql.connector

def get_airports_distance(icao):
    sql = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = "{icao}"'
    cursor = yhteys.cursor()
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    print(airport_data)
    return airport_data
def get_airport_distance2(icao2):
    sql = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = "{icao2}"'
    cursor = yhteys.cursor()
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    print(airport_data)
    return airport_data



yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='python',
    password='salasana',
    autocommit=True
)
icao = input("Anna lentokenttä1 icao koodi")
icao2 = input("Anna lentokenttä2 icao koodi")

tiedot1 = get_airports_distance(icao)
tiedot2 = get_airport_distance2(icao2)


print(f'lentokenttien etäisyys on {distance.distance(tiedot1, tiedot2).km:.2f} Kilometriä')