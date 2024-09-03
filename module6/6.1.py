import random
def dicer():
    heitto = random.randint(1,6)
    return heitto


luku = 0
while luku != 6:
    luku = dicer()
    print(luku)