import math

def pizzalaskuri(pizzahalk, hinta):
    r = pizzahalk/2
    pintaala = math.pi * r**2

    pintaeur = pintaala/hinta
    return pintaeur

pizzahalka = int(input("Anna ekan pizzan halkasija!: "))
eur = int(input("Anna ekan pizzan hinta!: "))

pizza1 = pizzalaskuri(pizzahalka, eur)

pizzahalka = int(input("Anna tokan pizzan halkasija!: "))
eur = int(input("Anna tokan pizzan hinta!: "))

pizza2 = pizzalaskuri(pizzahalka, eur)

if pizza1 > pizza2:
    print("ensinmäisessä pizzassa on parempi hintalaatu suhde!")
else:
    print("toisessa pizzassa on parempi hintalaatu suhde!")






