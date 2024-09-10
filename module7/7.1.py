vuodenajat = ("kevät", "kesä", "syksy", "talvi")
kuukausi = int(input("Anna kuukauden numero!: "))

talvi = (12, 1, 2)
kevät = (3, 4, 5)
kesä = (6, 7, 8)
syksy = (9, 10, 11)

if kuukausi in talvi:
    print("talvi")
elif kuukausi in kevät:
    print("kevät")
elif kuukausi in kesä:
    print("kesä")
else:
    print ("syksy")
