luvut=[]
while True:
    luku = (input("Anna Luku!: "))
    if luku == "":

        luvut.sort(reverse=True)
        print(luvut[0:5])
        break
    luku = int(luku)
    luvut.append(luku)



