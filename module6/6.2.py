import random
def dicer(nopmax):
    heitto = random.randint(1,nopmax)
    return heitto

noppamax = int(input("Anna noppan max silmäluku!: "))
luku = 0
while luku != noppamax:
    luku = dicer(noppamax)
    print(luku)





