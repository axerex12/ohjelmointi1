import random
N = int(input("Anna pisteiden määrä!: "))
tarkistaja =0
hitcircle = 0

while N>tarkistaja:
    tarkistaja = tarkistaja+1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <1:
        hitcircle +=1

piiliki = (4*hitcircle/N)
print(piiliki)