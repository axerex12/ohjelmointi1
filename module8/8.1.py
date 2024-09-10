import mysql.connector

def get_airport(icao):
    sql = f'SELECT name, municipality FROM airport WHERE ident = "{icao}"'
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    return airport_data


yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='python',
    password='salasana',
    autocommit=True
)
syöte = input("Anna lentokentän Icao Koodi: ")
airports = get_airport(syöte)
for airport in airports:
    print(f'nimi on {airport["name"]} ja sijaintikunta on {airport["municipality"]}')