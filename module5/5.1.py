import random


nopat=[]
noppia = int(input("Montako noppaa!: "))
for i in range(0, noppia):
    nopat.append(random.randint (1,6))
noppasumma = sum(nopat)
print(noppasumma)
print (nopat)