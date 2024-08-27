sentti = 2.54
x = 1
while x > 0:
    tuumat=float(input("Anna tuuma määrä!: "))
    if tuumat < 0:
        x = -1
        break
    print(tuumat*sentti)

