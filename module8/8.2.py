import mysql.connector

def get_airport_by_countrycode (countrycode):
    sql = f'SELECT type FROM airport WHERE iso_country = "{countrycode}"'
    cursor = yhteys.cursor()
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    print(sql)
    return airport_data

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='python',
    password='salasana',
    autocommit=True
)

smallport = 0
heliport = 0
maakoodi = input("Anna maa koodi!: ")
airports = get_airport_by_countrycode(maakoodi)
print(airports)
for airport in airports:
    if airport [0] == "small_airport":
        smallport +=1
    elif airport[0] == "heliport":
        heliport +=1
print(f'pieniä lentokenttiä on {smallport} kappaletta, helikopterikenttiä on {heliport} kappaletta')