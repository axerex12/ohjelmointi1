lentokoneasemat = {}
while True:
    syöte = int(input("Haluatko lisätä lentoaseman: syötä 1 haluatko hakea syötä 2 lopettaa? syötä 3"))
    if syöte == 1:
        ICAO = input("Anna lnetokentän ICAO koodi: ")
        lentkentnimi = input("Anna lentokentän nimi: ")
        lentokoneasemat[ICAO]=lentkentnimi
    elif syöte == 2:
        koodi = input("Anna ICAO koodi: ")
        if koodi in lentokoneasemat:
            print(lentokoneasemat[koodi])
        else:
            print("koodilla ei löytynyt lentokenttää")
    elif syöte == 3:
        break



