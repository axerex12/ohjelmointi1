suurin = "0"
numero = input("Anna numero!: ")
pienin = numero
while True:
    numero = input("Anna numero!: ")
    if numero == "":
        print(pienin, suurin)
        break
    if numero > suurin:
        suurin = numero
    if numero < pienin:
        pienin = numero


