import random
from random import randint

nopat=[]
noppia = int(input("Montako noppaa!: "))
for i in range(0, noppia):
    nopat.append(randint (1,6))
noppasumma = sum(nopat)
print(noppasumma)
print (nopat)